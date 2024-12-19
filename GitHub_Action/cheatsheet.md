# Location

`.github/workflows/`

# Demo

```yaml
name: learn-github-actions                                      # 1
run-name: ${{ github.actor }} is learning GitHub Actions        # 2
on: [push]                                                      # 3
jobs:                                                           # 4
  check-bats-version:                                           # 5
    runs-on: ubuntu-latest                                      # 6
    steps:                                                      # 7
      - uses: actions/checkout@v3                               # 8
      - uses: actions/setup-node@v3
        with:
          node-version: '14'

      - name: List files in the repository                      # 9
        run: |                                                  # 10
          ls ${{ github.workspace }}

      - run: npm install -g bats                                # 11
      - run: bats -v
```

1. Optional. The name of the workflow as it will appear in the "Actions" tab
2. Optional. The name for workflow runs. here we use `github` variable context. We can use [run-name](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#run-name) for display.
3. specifies what **triggers the github actions** 
4. `jobs`. Groups together all the jobs that run
5. `check-bats-version`, a name. Defines a job name
6. `runs-on`. Defines the OS type for the jobs to run on. There are [windows, linux-ubuntu, macOS](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#choosing-github-hosted-runners) 
7. `steps`. Groups all steps that run under the `check-bats-version` job.
8. `uses: actions/checkout@v3`, specifies this step will do `actions/checkout@v3`. This is an action that checks out your repository onto the runner, allowing you to run scripts or other actions against your code (such as build and test tools).
9. `name`. Name of the step
10. `run`, the command in the system. Here we use `ls`.
11. `run` run the commands without name

## Environment variable

We here set the postgresql environment variable.
```
jobs:
  example-job:
      steps:
        - name: Connect to PostgreSQL
          run: node client.js
          env:
            POSTGRES_HOST: postgres
            POSTGRES_PORT: 5432
```

## Add scripts to workflow

Here we add a script in the repository, and we use the jobs to run it.
```
jobs:
  example-job:
    steps:
      - name: Run build script
        run: ./.github/scripts/build.sh
        shell: bash
```
