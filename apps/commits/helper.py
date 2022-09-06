import pandas as pd
from .models import GitCommits


def commits_of_repo_github(repo, owner, api, gh_session):
    commits = []
    next = True
    i = 1
    while next == True:
        url = f"{api}/repos/{owner}/{repo}/commits?page={i}"
        commit_pg = gh_session.get(url=url)

        if commit_pg.status_code == 200:
            commit_pg_list = [
                dict(item, **{'repo_name': '{}'.format(repo)}) for item in commit_pg.json()]
            commit_pg_list = [
                dict(item, **{'owner': '{}'.format(owner)}) for item in commit_pg_list]
            commits = commits + commit_pg_list
            if 'Link' in commit_pg.headers:
                if 'rel="next"' not in commit_pg.headers['Link']:
                    next = False
            i = i + 1

        else:
            next = False
            return "Error in fetching commits"

    commit_json = []
    for data in commits:
        commit_json.append({
            'commit_sha': data['sha'],
            'commit_message': data['commit']['message'],
            'commit_date': str(data['commit']['author']['date']),
            'commit_author_name': data['commit']['author']['name'],
            'commit_author_email': data['commit']['author']['email'],
            'commit_committer_name': data['commit']['committer']['name'],
            'commit_committer_email': data['commit']['committer']['email'],
            'repo_name': data['repo_name'],
            'owner': data['owner'],
        })

    # insert only if there are new commits
    if len(commit_json) > 0:
        df = pd.DataFrame(commit_json)
        df['commit_date'] = pd.to_datetime(df['commit_date'])
        df = df.drop_duplicates(subset=['commit_sha'])
        df = df.sort_values(by=['commit_date'])
        # convert commit_date to string
        df['commit_date'] = df['commit_date'].dt.strftime('%Y-%m-%d %H:%M:%S')
        df = df.reset_index(drop=True)
        df['commit_id'] = df.index + 1

        df = df[[
            'commit_id', 'commit_sha', 'commit_message', 'commit_date', 'commit_author_name',
            'commit_author_email', 'commit_committer_name', 'commit_committer_email', 'repo_name', 'owner'
        ]]

        # compare with existing commits_sha in database and insert only new commits
        existing_commits = GitCommits.objects.get_queryset().values_list(
            'commit_sha', flat=True)
        df = df[~df['commit_sha'].isin(existing_commits)]
        print(f"Inserting {(df.to_dict(orient='records'))} new commits")

        # insert new commits
        GitCommits.objects.bulk_create(
            GitCommits(**row) for row in df.to_dict(orient='records'))

        return df.to_dict(orient='records')

    else:
        return "No new commits"
