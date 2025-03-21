# Contributing

Welcome to `ac-microcourses` contributor's guide.

This document focuses on getting any potential contributor familiarized with
the development processes, but [other kinds of contributions] are also appreciated.

If you are new to using [git] or have never collaborated in a project previously,
please have a look at [contribution-guide.org]. Other resources are also
listed in the excellent [guide created by FreeCodeCamp] [^contrib1].

Please notice, all users and contributors are expected to be **open,
considerate, reasonable, and respectful**. When in doubt,
[Python Software Foundation's Code of Conduct] is a good reference in terms of
behavior guidelines.

## Issue Reports

If you experience bugs or general issues with `ac-microcourses`, please have a look
on the [issue tracker].
If you don't see anything useful there, please feel free to fire an issue report.

:::{tip}
Please don't forget to include the closed issues in your search.
Sometimes a solution was already reported, and the problem is considered
**solved**.
:::

New issue reports should include information about your programming environment
(e.g., operating system, Python version) and steps to reproduce the problem.
Please try also to simplify the reproduction steps to a very minimal example
that still illustrates the problem you are facing. By removing other factors,
you help us to identify the root cause of the issue.

## Documentation Improvements

You can help improve `ac-microcourses` docs by making them more readable and coherent, or
by adding missing information and correcting mistakes.

`ac-microcourses` documentation uses [Sphinx] as its main documentation
compiler. This means that the docs are kept in the same repository as the
project code, and that any documentation update is done in the same way was a
code contribution. The markup language used is [CommonMark] with [MyST]
extensions.

:::{tip}
   Please notice that the [GitHub web interface] provides a quick way of
   propose changes in `ac-microcourses`'s files. While this mechanism can
   be tricky for normal code contributions, it works perfectly fine for
   contributing to the docs, and can be quite handy.

   If you are interested in trying this method out, please navigate to
   the `docs` folder in the source [repository], find which file you
   would like to propose changes and click in the little pencil icon at the
   top, to open [GitHub's code editor]. Once you finish editing the file,
   please write a message in the form at the bottom of the page describing
   which changes have you made and what are the motivations behind them and
   submit your proposal.
:::

When working on documentation changes in your local machine, you can
compile them using [tox] :

```
tox -e docs
```

and use Python's built-in web server for a preview in your web browser
(`http://localhost:8000`):

```
python3 -m http.server --directory 'docs/_build/html'
```

## Code Contributions

Courses are divided into modules, where each module typically contains a
tutorial, a quiz, and an assignment. Tutorials contain text and video resources
and often a hands-on and bare bones implementation of the concept being covered.
The tutorial also provides links to quizzes which are hosted on Quercus, and
links to assignments which are hosted through GitHub Classroom.

Most of the content in this repo is contained within the `docs` folder. Each
course has it's own folder within `docs/courses/` (e.g.,
`docs/courses/hello-world`).

Index and overview files are generated automatically via Jinja2 templates
contained within `src/ac_microcourses` via `scripts/generate_overviews.py`. This
script is run automatically via the Makefile when building the docs.

### Submit an issue

Before you work on any non-trivial code contribution it's best to first create
a report in the [issue tracker] to start a discussion on the subject.
This often provides additional considerations and avoids unnecessary work.

### Create an environment

Before you start coding, we recommend creating an isolated [virtual environment]
to avoid any problems with your installed Python packages.
This can easily be done via either [virtualenv]:

```
virtualenv <PATH TO VENV>
source <PATH TO VENV>/bin/activate
```

or [Miniconda]:

```
conda create -n ac-microcourses python=3 six virtualenv pytest pytest-cov
conda activate ac-microcourses
```

### Clone the repository

1. Create an user account on GitHub if you do not already have one.

2. Fork the project [repository]: click on the *Fork* button near the top of the
   page. This creates a copy of the code under your account on GitHub.

3. Clone this copy to your local disk:

   ```
   git clone git@github.com:YourLogin/ac-microcourses.git
   cd ac-microcourses
   ```

4. You should run:

   ```
   pip install -U pip setuptools -e .
   ```

   to be able to import the package under development in the Python REPL.

5. Install [pre-commit]:

   ```
   pip install pre-commit
   pre-commit install
   ```

   `ac-microcourses` comes with a lot of hooks configured to automatically help the
   developer to check the code being written.

### Implement your changes

1. Create a branch to hold your changes:

   ```
   git checkout -b my-feature
   ```

   and start making changes. Never work on the main branch!

2. Start your work on this branch. Don't forget to add [docstrings] to new
   functions, modules and classes, especially if they are part of public APIs.

3. Add yourself to the list of contributors in `AUTHORS.rst`.

4. When you’re done editing, do:

   ```
   git add <MODIFIED FILES>
   git commit
   ```

   to record your changes in [git].

   Please make sure to see the validation messages from [pre-commit] and fix
   any eventual issues.
   This should automatically use [flake8]/[black] to check/fix the code style
   in a way that is compatible with the project.

   :::{important}
   Don't forget to add unit tests and documentation in case your
   contribution adds an additional feature and is not just a bugfix.

   Moreover, writing a [descriptive commit message] is highly recommended.
   In case of doubt, you can check the commit history with:

   ```
   git log --graph --decorate --pretty=oneline --abbrev-commit --all
   ```

   to look for recurring communication patterns.
   :::

5. Please check that your changes don't break any unit tests with:

   ```
   tox
   ```

   (after having installed [tox] with `pip install tox` or `pipx`).

   You can also use [tox] to run several other pre-configured tasks in the
   repository. Try `tox -av` to see a list of the available checks.

### Submit your contribution

1. If everything works fine, push your local branch to the remote server with:

   ```
   git push -u origin my-feature
   ```

2. Go to the web page of your fork and click "Create pull request"
   to send your changes for review.

   Find more detailed information in [creating a PR]. You might also want to open
   the PR as a draft first and mark it as ready for review after the feedbacks
   from the continuous integration (CI) system or any required fixes.

### Troubleshooting

The following tips can be used when facing problems to build or test the
package:

1. Make sure to fetch all the tags from the upstream [repository].
   The command `git describe --abbrev=0 --tags` should return the version you
   are expecting. If you are trying to run CI scripts in a fork repository,
   make sure to push all the tags.
   You can also try to remove all the egg files or the complete egg folder, i.e.,
   `.eggs`, as well as the `*.egg-info` folders in the `src` folder or
   potentially in the root of your project.

2. Sometimes [tox] misses out when new dependencies are added, especially to
   `setup.cfg` and `docs/requirements.txt`. If you find any problems with
   missing dependencies when running a command with [tox], try to recreate the
   `tox` environment using the `-r` flag. For example, instead of:

   ```
   tox -e docs
   ```

   Try running:

   ```
   tox -r -e docs
   ```

3. Make sure to have a reliable [tox] installation that uses the correct
   Python version (e.g., 3.7+). When in doubt you can run:

   ```
   tox --version
   # OR
   which tox
   ```

   If you have trouble and are seeing weird errors upon running [tox], you can
   also try to create a dedicated [virtual environment] with a [tox] binary
   freshly installed. For example:

   ```
   virtualenv .venv
   source .venv/bin/activate
   .venv/bin/pip install tox
   .venv/bin/tox -e all
   ```

4. [Pytest can drop you] in an interactive session in the case an error occurs.
   In order to do that you need to pass a `--pdb` option (for example by
   running `tox -- -k <NAME OF THE FALLING TEST> --pdb`).
   You can also setup breakpoints manually instead of using the `--pdb` option.

## Maintainer tasks

### Releases

If you are part of the group of maintainers and have correct user permissions
on [PyPI], the following steps can be used to release a new version for
`ac-microcourses`:

1. Make sure all unit tests are successful.
2. Tag the current commit on the main branch with a release tag, e.g., `v1.2.3`.
3. Push the new tag to the upstream [repository],
   e.g., `git push upstream v1.2.3`
4. Clean up the `dist` and `build` folders with `tox -e clean`
   (or `rm -rf dist build`)
   to avoid confusion with old builds and Sphinx docs.
5. Run `tox -e build` and check that the files in `dist` have
   the correct version (no `.dirty` or [git] hash) according to the [git] tag.
   Also check the sizes of the distributions, if they are too big (e.g., >
   500KB), unwanted clutter may have been accidentally included.
6. Run `tox -e publish -- --repository pypi` and check that everything was
   uploaded to [PyPI] correctly.


### New Courses

Create a new GitHub organization (e.g., https://github.com/orgs/ACC-HelloWorld/ and https://github.com/ACC-DataScience). Free organization. Tied to personal account. Add corresponding emoji as profile picture (PPT --> fill white background, copy-paste as image, crop, save as image, org settings, upload profile picture). Organization display name of form `AC Classroom - Hello World`. URL is the specific microcourse URL (e.g., https://ac-microcourses.readthedocs.io/en/latest/courses/hello-world/overview.html).

- https://github.com/ACC-HelloWorld
- https://github.com/ACC-DataScience
- https://github.com/ACC-Robotics
- https://github.com/ACC-SoftwareDev
- https://github.com/ACC-DesignProject

There is also a parent-level organization: https://github.com/AC-Classroom. This is where base templates go.

Within https://classroom.github.com/, "New Classroom". Pick the corresponding organization. Of the form `robotics-8a3a78` (i.e., can keep the random ID that's autogenerated).

"TAs" would need admin access to the organization, then send the TAs the classroom invitation URL.

Add roster entries manually (can upload a CSV). I use [adj-noun-pairs.csv](./notebooks/adj-noun-pairs.csv) which has 500. It's a bit unwieldy, but scalable.

For the first assignment, go to the existing assignment from one of the courses and click "Edit" then "Reuse assignment". At minimum, do this for 0.1 (intro git and GitHub), 0.2 (intro to GitHub Classroom), and 0.3 (Python refresher). If the copy fails, just make a new assignment and manually mirror the settings for the assignment you're trying to copy. Note that when you "reuse an assignment" it creates templates in your new organization, so make sure that you actually want the same repo as the one that was used in the original assignment. Otherwise, start from scratch and copy over settings as needed.

Enable GitHub Codespaces on the organization level (free assuming academic organization). "Upgrade this organization to GitHub Team for free to use this feature". Also, on the GitHub organization settings, change to "Organization ownership" (e.g., https://github.com/organizations/ACC-Robotics/settings/codespaces).

Related, e.g.,: https://classroom.github.com/classrooms/180682108-robotics-8a3a78/settings.

You need to complete the above step for the organization before you can choose GitHub Codespaces as the supported editor for an assignment.

Typically, for each assignment, you'll need to create a new repository within the organization. Go to https://github.com/AC-Classroom/autograding-codespace-python and click "use this template" --> "create a new repository". Owner should be the organization. Name it e.g., `1-pumps-and-pipettes`, keep it private. Then, go to settings and check the box for "template repository". This is necessary for it to be used by GitHub Classroom.

You'll add this repo as the starter code to the GitHub Classroom assignment. Update that repo with your assignment content. Typically, you'll also grant students admin access to the repositories so that they can do things like add repo secrets. Usually, copy the default branch only.

For autograding tests, typically I use `sudo -H pip3 install -r requirements.txt` for the setup command (even though it says don't use sudo, and use pip instead of pip3). This was due to some intricate things with installing local packages and getting both Codespaces and GitHub Actions to deal with these local installations appropriately. Perhaps there's a workaround. A typical name: `Multi-task test suite` (also `Pumps and pipettes test suite`). A timeout of 5 and a point value of 10 is typical.

Usually, you'll want to assign partial points. You can do this by using a `run_command` preset (instead of `Python` preset) with a command such as `pytest bayesian_optimization_test.py::test_parameters_and_objectives`. There may be some potential to refactor things to use Custom YAML instead.

### Syncing changes between parent template, gh classroom copy, and student forks

Based on https://chatgpt.com/share/67c0233e-a684-8006-a5a9-41affa40cf8d, ported from https://github.com/AccelerationConsortium/ac-microcourses/issues/149.

After creating a codespace (or cloning locally) for the private repo (the one that GitHub Classroom autogenerates when the instructor first creates an assignment):

```bash
git remote add upstream https://github.com/template-owner/template-repo.git
```

Verify the remotes:
```bash
git remote -v
```

Which should look something like:
```bash
origin   https://github.com/your-username/your-private-repo.git (fetch)
origin   https://github.com/your-username/your-private-repo.git (push)
upstream https://github.com/template-owner/template-repo.git (fetch)
upstream https://github.com/template-owner/template-repo.git (push)
```

Fetch the latest from the template repo.

```bash
git fetch upstream
```

Merge.

```bash
git merge upstream/main --squash --allow-unrelated-histories
```

Resolve the conflicts by right clicking on each file in the Codespace source control sidebar that has an exclamation mark icon, and selecting **accept all incoming**. Remember to save the actual file in the editor. Do this for all files (assuming you haven't made any changes on the autogenerated file that you want to keep, otherwise use merge editor), and then stage all files. NOTE: The merge conflicts should have gone away. If you haven't saved all the files, then it will likely throw a warning or error. Don't commit if there are still unresolved merge conflicts. Finally, commit the files and sync.

Back in the GitHub Classroom interface for the assignment, you'll click "sync assignments. After "sync assignments" via GitHub Classroom, then there might be merge conflicts on some of the student repositories. If the student has already started working on the assignment, things get tricky. If only files other than the ones the student should be editing are changed, then the solution seems to be to open that PR, manually look through the edits, and merge. If the student has started working on the assignment, then instead of merging the PR, you'll manually apply the changes directly to the main branch (not in the context of the PR) and then close the PR. This has to do with the fact that if you edit the file, the changes would go back to the autogenerated GitHub Classroom assignment repo (private template repo), which isn't what we want.

If the student hasn't started working on the assignment, hopefully these have the "resolve in editor" button (i.e., without needing to clone or go to a codespace) when navigating to the pull request, at which point you can generally accept current for wherever the student's solution has already been applied, though there may be some cases which require special attention. The issue is that this process will need to be taken care of for each repository this applies to, either by the student or by the instructor. It may not matter as much for students who have already completed and passed an assignment, unless that assignment grade is directly passed via API to the learning management system (right now, it's a manual self-report).


[^contrib1]: Even though, these resources focus on open source projects and
    communities, the general ideas behind collaborating with other developers
    to collectively create software are general and can be applied to all sorts
    of environments, including private companies and proprietary code bases.

[black]: https://pypi.org/project/black/
[commonmark]: https://commonmark.org/
[contribution-guide.org]: http://www.contribution-guide.org/
[creating a pr]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request
[descriptive commit message]: https://chris.beams.io/posts/git-commit
[docstrings]: https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html
[first-contributions tutorial]: https://github.com/firstcontributions/first-contributions
[flake8]: https://flake8.pycqa.org/en/stable/
[git]: https://git-scm.com
[github web interface]: https://docs.github.com/en/github/managing-files-in-a-repository/managing-files-on-github/editing-files-in-your-repository
[github's code editor]: https://docs.github.com/en/github/managing-files-in-a-repository/managing-files-on-github/editing-files-in-your-repository
[github's fork and pull request workflow]: https://guides.github.com/activities/forking/
[guide created by freecodecamp]: https://github.com/freecodecamp/how-to-contribute-to-open-source
[miniconda]: https://docs.conda.io/en/latest/miniconda.html
[myst]: https://myst-parser.readthedocs.io/en/latest/syntax/syntax.html
[other kinds of contributions]: https://opensource.guide/how-to-contribute
[pre-commit]: https://pre-commit.com/
[pypi]: https://pypi.org/
[pyscaffold's contributor's guide]: https://pyscaffold.org/en/stable/contributing.html
[pytest can drop you]: https://docs.pytest.org/en/stable/usage.html#dropping-to-pdb-python-debugger-at-the-start-of-a-test
[python software foundation's code of conduct]: https://www.python.org/psf/conduct/
[restructuredtext]: https://www.sphinx-doc.org/en/master/usage/restructuredtext/
[sphinx]: https://www.sphinx-doc.org/en/master/
[tox]: https://tox.readthedocs.io/en/stable/
[virtual environment]: https://realpython.com/python-virtual-environments-a-primer/
[virtualenv]: https://virtualenv.pypa.io/en/stable/

[repository]: https://github.com/AccelerationConsortium/ac-microcourses
[issue tracker]: https://github.com/AccelerationConsortium/ac-microcourses/issues
