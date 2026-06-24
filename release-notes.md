# Release Notes

## Latest Changes

### Features

* ♻️ Add support for Python 3.12. PR [#228](https://github.com/tiangolo/uwsgi-nginx-docker/pull/228) by [@tiangolo](https://github.com/tiangolo).
* 🔧 Avoid creating unnecessary `*.pyc` files with `PYTHONDONTWRITEBYTECODE=1` and ensure logs are printed immediately with `PYTHONUNBUFFERED=1`. PR [#208](https://github.com/tiangolo/uwsgi-nginx-docker/pull/208) by [@estebanx64](https://github.com/estebanx64).

### Refactors

* ♻️ Do not `EXPOSE` ports `80` and `443` by default as they can be customized. PR [#227](https://github.com/tiangolo/uwsgi-nginx-docker/pull/227) by [@tiangolo](https://github.com/tiangolo).

### Upgrades

* ⬆ Bump uwsgi from 2.0.30 to 2.0.31. PR [#247](https://github.com/tiangolo/uwsgi-nginx-docker/pull/247) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆️ Upgrade Nginx to latest, `1.29.3`, and Debian to latest, Trixie. PR [#248](https://github.com/tiangolo/uwsgi-nginx-docker/pull/248) by [@tiangolo](https://github.com/tiangolo).
* ⬆ Bump uwsgi from 2.0.29 to 2.0.30. PR [#240](https://github.com/tiangolo/uwsgi-nginx-docker/pull/240) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump uwsgi from 2.0.28 to 2.0.29. PR [#237](https://github.com/tiangolo/uwsgi-nginx-docker/pull/237) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆️ Upgrade Docker images to Debian Bookworm and latest Nginx. PR [#238](https://github.com/tiangolo/uwsgi-nginx-docker/pull/238) by [@tiangolo](https://github.com/tiangolo).
* ⬆ Bump uwsgi from 2.0.26 to 2.0.28. PR [#232](https://github.com/tiangolo/uwsgi-nginx-docker/pull/232) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 🔥 Drop support for Python 3.7 and 3.8. PR [#233](https://github.com/tiangolo/uwsgi-nginx-docker/pull/233) by [@tiangolo](https://github.com/tiangolo).
* ⬆ Bump uwsgi from 2.0.22 to 2.0.26. PR [#210](https://github.com/tiangolo/uwsgi-nginx-docker/pull/210) by [@dependabot[bot]](https://github.com/apps/dependabot).

### Docs

* 📝 Add note about historical README. PR [#251](https://github.com/tiangolo/uwsgi-nginx-docker/pull/251) by [@tiangolo](https://github.com/tiangolo).
* 📝 Add deprecation note. PR [#250](https://github.com/tiangolo/uwsgi-nginx-docker/pull/250) by [@tiangolo](https://github.com/tiangolo).

### Internal

* 👷 Simplify pull request workflow triggers. PR [#271](https://github.com/tiangolo/uwsgi-nginx-docker/pull/271) by [@tiangolo](https://github.com/tiangolo).
* 👷 Update setup-python pin comment to 6.2.0. PR [#270](https://github.com/tiangolo/uwsgi-nginx-docker/pull/270) by [@tiangolo](https://github.com/tiangolo).
* 📝 Refactor release notes, move to its own file. PR [#269](https://github.com/tiangolo/uwsgi-nginx-docker/pull/269) by [@tiangolo](https://github.com/tiangolo).
* 👷 Update issue-manager to 0.7.1. PR [#268](https://github.com/tiangolo/uwsgi-nginx-docker/pull/268) by [@tiangolo](https://github.com/tiangolo).
* ⬆️ Update issue-manager to 0.7.0. PR [#267](https://github.com/tiangolo/uwsgi-nginx-docker/pull/267) by [@tiangolo](https://github.com/tiangolo).
* 🔒️ Add zizmor workflow security checks. PR [#265](https://github.com/tiangolo/uwsgi-nginx-docker/pull/265) by [@tiangolo](https://github.com/tiangolo).
* ⬆ Bump the github-actions group across 1 directory with 3 updates. PR [#263](https://github.com/tiangolo/uwsgi-nginx-docker/pull/263) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 🔥 Remove configs now stored in central GitHub repo. PR [#260](https://github.com/tiangolo/uwsgi-nginx-docker/pull/260) by [@tiangolo](https://github.com/tiangolo).
* 👷 Update Dependabot. PR [#259](https://github.com/tiangolo/uwsgi-nginx-docker/pull/259) by [@tiangolo](https://github.com/tiangolo).
* ⬆ Bump docker/setup-buildx-action from 3 to 4. PR [#257](https://github.com/tiangolo/uwsgi-nginx-docker/pull/257) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump docker/build-push-action from 6 to 7. PR [#258](https://github.com/tiangolo/uwsgi-nginx-docker/pull/258) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump actions/checkout from 5 to 6. PR [#253](https://github.com/tiangolo/uwsgi-nginx-docker/pull/253) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump peter-evans/dockerhub-description from 4 to 5. PR [#252](https://github.com/tiangolo/uwsgi-nginx-docker/pull/252) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 👷 Upgrade actions/checkout from v5 to v6. PR [#255](https://github.com/tiangolo/uwsgi-nginx-docker/pull/255) by [@tiangolo](https://github.com/tiangolo).
* 👷 Upgrade `latest-changes` GitHub Action and pin `actions/checkout@v5`. PR [#254](https://github.com/tiangolo/uwsgi-nginx-docker/pull/254) by [@tiangolo](https://github.com/tiangolo).
* 🔥 Drop support for Python 3.9. PR [#249](https://github.com/tiangolo/uwsgi-nginx-docker/pull/249) by [@tiangolo](https://github.com/tiangolo).
* ⬆ Bump actions/checkout from 4 to 5. PR [#243](https://github.com/tiangolo/uwsgi-nginx-docker/pull/243) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump actions/labeler from 5 to 6. PR [#244](https://github.com/tiangolo/uwsgi-nginx-docker/pull/244) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump actions/setup-python from 5 to 6. PR [#245](https://github.com/tiangolo/uwsgi-nginx-docker/pull/245) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump tiangolo/issue-manager from 0.5.1 to 0.6.0. PR [#246](https://github.com/tiangolo/uwsgi-nginx-docker/pull/246) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump tiangolo/latest-changes from 0.3.2 to 0.4.0. PR [#242](https://github.com/tiangolo/uwsgi-nginx-docker/pull/242) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 👷 Add CI Labeler. PR [#236](https://github.com/tiangolo/uwsgi-nginx-docker/pull/236) by [@tiangolo](https://github.com/tiangolo).
* ⬆ Bump tiangolo/latest-changes from 0.3.1 to 0.3.2. PR [#235](https://github.com/tiangolo/uwsgi-nginx-docker/pull/235) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 🔥 Remove old unused files. PR [#234](https://github.com/tiangolo/uwsgi-nginx-docker/pull/234) by [@tiangolo](https://github.com/tiangolo).
* ⬆ Bump tiangolo/issue-manager from 0.5.0 to 0.5.1. PR [#229](https://github.com/tiangolo/uwsgi-nginx-docker/pull/229) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump docker/build-push-action from 5 to 6. PR [#225](https://github.com/tiangolo/uwsgi-nginx-docker/pull/225) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 👷 Update `issue-manager.yml`. PR [#226](https://github.com/tiangolo/uwsgi-nginx-docker/pull/226) by [@tiangolo](https://github.com/tiangolo).
* ⬆ Bump docker/login-action from 1 to 3. PR [#204](https://github.com/tiangolo/uwsgi-nginx-docker/pull/204) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump peter-evans/dockerhub-description from 3 to 4. PR [#205](https://github.com/tiangolo/uwsgi-nginx-docker/pull/205) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump docker/setup-buildx-action from 1 to 3. PR [#206](https://github.com/tiangolo/uwsgi-nginx-docker/pull/206) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump docker/build-push-action from 2 to 5. PR [#207](https://github.com/tiangolo/uwsgi-nginx-docker/pull/207) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 👷 Update `latest-changes` GitHub Action. PR [#214](https://github.com/tiangolo/uwsgi-nginx-docker/pull/214) by [@tiangolo](https://github.com/tiangolo).
* 👷 Update issue-manager.yml GitHub Action permissions. PR [#213](https://github.com/tiangolo/uwsgi-nginx-docker/pull/213) by [@tiangolo](https://github.com/tiangolo).
* 🔧 Add GitHub templates for discussions and issues, and security policy. PR [#203](https://github.com/tiangolo/uwsgi-nginx-docker/pull/203) by [@alejsdev](https://github.com/alejsdev).
* 🔧 Update `latest-changes.yml`. PR [#201](https://github.com/tiangolo/uwsgi-nginx-docker/pull/201) by [@alejsdev](https://github.com/alejsdev).

## 2.1.0

### Features

* ✨ Add support for multiarch builds, including ARM (e.g. Mac M1). PR [#200](https://github.com/tiangolo/uwsgi-nginx-docker/pull/200) by [@tiangolo](https://github.com/tiangolo).

### Refactors

* 🔥 Remove support for Alpine. PR [#198](https://github.com/tiangolo/uwsgi-nginx-docker/pull/198) by [@tiangolo](https://github.com/tiangolo).

### Upgrades

* ⬆️ Bump uwsgi from 2.0.21 to 2.0.22 in /docker-images. PR [#188](https://github.com/tiangolo/uwsgi-nginx-docker/pull/188) by [@dependabot[bot]](https://github.com/apps/dependabot).

### Docs

* 📝 Update test badge in `README.md`. PR [#199](https://github.com/tiangolo/uwsgi-nginx-docker/pull/199) by [@alejsdev](https://github.com/alejsdev).

### Internal

* 👷 Update dependabot. PR [#183](https://github.com/tiangolo/uwsgi-nginx-docker/pull/183) by [@tiangolo](https://github.com/tiangolo).
* 👷 Update latest changes token. PR [#180](https://github.com/tiangolo/uwsgi-nginx-docker/pull/180) by [@tiangolo](https://github.com/tiangolo).
* 👷 Add GitHub Action for Docker Hub description. PR [#172](https://github.com/tiangolo/uwsgi-nginx-docker/pull/172) by [@tiangolo](https://github.com/tiangolo).
* ⬆ Bump actions/checkout from 3.1.0 to 4.1.2. PR [#197](https://github.com/tiangolo/uwsgi-nginx-docker/pull/197) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump tiangolo/issue-manager from 0.4.1 to 0.5.0. PR [#193](https://github.com/tiangolo/uwsgi-nginx-docker/pull/193) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump peter-evans/dockerhub-description from 3 to 4. PR [#192](https://github.com/tiangolo/uwsgi-nginx-docker/pull/192) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump actions/setup-python from 4 to 5. PR [#189](https://github.com/tiangolo/uwsgi-nginx-docker/pull/189) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump tiangolo/issue-manager from 0.4.0 to 0.4.1. PR [#191](https://github.com/tiangolo/uwsgi-nginx-docker/pull/191) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 👷 Update latest-changes GitHub Action. PR [#182](https://github.com/tiangolo/uwsgi-nginx-docker/pull/182) by [@tiangolo](https://github.com/tiangolo).

## 2.0.0

Highlights of this release:

* Support for Python 3.10, 3.11, and 3.9.
* Deprecation of Python 3.6 and 2.7.
    * The last Python 3.6 and 2.7 images are available in Docker Hub, but they won't be updated or maintained anymore.
    * The last images with a date tag are `python3.6-2022-11-25` and `python2.7-2022-11-25`.
* Upgraded versions of all the dependencies.
* Small improvements and fixes.

### Features

* ✨ Add support for Python 3.11. PR [#171](https://github.com/tiangolo/uwsgi-nginx-docker/pull/171) by [@tiangolo](https://github.com/tiangolo).
* ✨ Add support for Python 3.10 and upgrade uWSGI to `2.0.20`. PR [#127](https://github.com/tiangolo/uwsgi-nginx-docker/pull/127) by [@tiangolo](https://github.com/tiangolo).
* ⬆️ Update pip install command with flag --no-cache-dir to reduce disk used. PR [#120](https://github.com/tiangolo/uwsgi-nginx-docker/pull/120) by [@tiangolo](https://github.com/tiangolo).
* ✨ Quit Supervisor on errors, to allow orchestrators to handle it. PR [#110](https://github.com/tiangolo/uwsgi-nginx-docker/pull/110) by [@tiangolo](https://github.com/tiangolo).
* ✨ Add Python 3.9. PR [#101](https://github.com/tiangolo/uwsgi-nginx-docker/pull/101) by [@sjadema](https://github.com/sjadema).

### Breaking Changes

* 🔥 Deprecate and remove Python 3.6 and 2.7. PR [#164](https://github.com/tiangolo/uwsgi-nginx-docker/pull/164) by [@tiangolo](https://github.com/tiangolo).
* 🔥 Remove support for Python 2.7. PR [#123](https://github.com/tiangolo/uwsgi-nginx-docker/pull/123) by [@tiangolo](https://github.com/tiangolo).

### Upgrades

* ⬆️ Upgrade Nginx to the latest version 1.23.2, and Debian to bullseye. PR [#163](https://github.com/tiangolo/uwsgi-nginx-docker/pull/163) by [@tiangolo](https://github.com/tiangolo).
* ⬆️ Bump uwsgi from 2.0.20 to 2.0.21. PR [#159](https://github.com/tiangolo/uwsgi-nginx-docker/pull/159) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Upgrade Nginx to version 1.21.6 and Alpine to version 3.13. PR [#148](https://github.com/tiangolo/uwsgi-nginx-docker/pull/148) by [@haley-comet](https://github.com/haley-comet).
* ⬆ Upgrade Nginx to the latest version of the official images. PR [#107](https://github.com/tiangolo/uwsgi-nginx-docker/pull/107) by [@tiangolo](https://github.com/tiangolo).

### Docs

* 📝 Add note to discourage Alpine with Python. PR [#124](https://github.com/tiangolo/uwsgi-nginx-docker/pull/124) by [@tiangolo](https://github.com/tiangolo).
* 📝 Add Kubernetes warning, when to use this image. PR [#122](https://github.com/tiangolo/uwsgi-nginx-docker/pull/122) by [@tiangolo](https://github.com/tiangolo).
* ✏️ Fix typo duplicate "Note" in Readme. PR [#121](https://github.com/tiangolo/uwsgi-nginx-docker/pull/121) by [@tiangolo](https://github.com/tiangolo).
* 🐛 Fix broken link to TechEmpower benchmarks. PR [#96](https://github.com/tiangolo/uwsgi-nginx-docker/pull/96) by [@tiangolo](https://github.com/tiangolo).

### Internal

* ⬆️ Update autoflake requirement from ^1.3.1 to ^2.0.0. PR [#166](https://github.com/tiangolo/uwsgi-nginx-docker/pull/166) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆️ Update mypy requirement from ^0.971 to ^0.991. PR [#167](https://github.com/tiangolo/uwsgi-nginx-docker/pull/167) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆️ Update docker requirement from ^5.0.3 to ^6.0.1. PR [#168](https://github.com/tiangolo/uwsgi-nginx-docker/pull/168) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆️ Update black requirement from ^20.8b1 to ^22.10. PR [#169](https://github.com/tiangolo/uwsgi-nginx-docker/pull/169) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆️ Upgrade CI OS. PR [#170](https://github.com/tiangolo/uwsgi-nginx-docker/pull/170) by [@tiangolo](https://github.com/tiangolo).
* 🔧 Update Dependabot config. PR [#165](https://github.com/tiangolo/uwsgi-nginx-docker/pull/165) by [@tiangolo](https://github.com/tiangolo).
* ⬆️ Bump tiangolo/issue-manager from 0.2.0 to 0.4.0. PR [#112](https://github.com/tiangolo/uwsgi-nginx-docker/pull/112) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 👷 Add scheduled CI. PR [#162](https://github.com/tiangolo/uwsgi-nginx-docker/pull/162) by [@tiangolo](https://github.com/tiangolo).
* 👷 Add alls-green GitHub Action. PR [#161](https://github.com/tiangolo/uwsgi-nginx-docker/pull/161) by [@tiangolo](https://github.com/tiangolo).
* ⬆️ Update black requirement from ^19.10b0 to ^20.8b1. PR [#116](https://github.com/tiangolo/uwsgi-nginx-docker/pull/116) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆️ Update isort requirement from ^4.3.21 to ^5.8.0. PR [#118](https://github.com/tiangolo/uwsgi-nginx-docker/pull/118) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆️ Update docker requirement from ^4.2.0 to ^5.0.3. PR [#126](https://github.com/tiangolo/uwsgi-nginx-docker/pull/126) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆️ Bump actions/setup-python from 1 to 4.1.0. PR [#155](https://github.com/tiangolo/uwsgi-nginx-docker/pull/155) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆️ Update mypy requirement from ^0.770 to ^0.971. PR [#156](https://github.com/tiangolo/uwsgi-nginx-docker/pull/156) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆️ Update pytest requirement from ^5.4.1 to ^7.0.1. PR [#138](https://github.com/tiangolo/uwsgi-nginx-docker/pull/138) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆️ Bump actions/checkout from 2 to 3.1.0. PR [#157](https://github.com/tiangolo/uwsgi-nginx-docker/pull/157) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 🔧 Run tests only on PRs or when pushing on master to avoid double CI. PR [#149](https://github.com/tiangolo/uwsgi-nginx-docker/pull/149) by [@tiangolo](https://github.com/tiangolo).
* 👷 Update Latest Changes GitHub Action. PR [#119](https://github.com/tiangolo/uwsgi-nginx-docker/pull/119) by [@tiangolo](https://github.com/tiangolo).
* 👷 Add Dependabot and external dependencies, to get automatic upgrade PRs. PR [#111](https://github.com/tiangolo/uwsgi-nginx-docker/pull/111) by [@tiangolo](https://github.com/tiangolo).
* 👷 Add GitHub Action latest-changes, update issue-manager. PR [#92](https://github.com/tiangolo/uwsgi-nginx-docker/pull/92) by [@tiangolo](https://github.com/tiangolo).
* Fix Python 3.8 Alpine environment for installed packages. PR [#84](https://github.com/tiangolo/uwsgi-nginx-docker/pull/84).

## 1.4.0

* Add [GitHub Sponsors](https://github.com/sponsors/tiangolo) button.
* Add new image for Python 3.8, and new image for Python 3.8 on Alpine. PR [#83](https://github.com/tiangolo/uwsgi-nginx-docker/pull/83).
* Upgrade Nginx to latest version, `1.17.10`, based on latest Debian, Buster. PR [#82](https://github.com/tiangolo/uwsgi-nginx-docker/pull/82).
* Remove support for Python 3.5. PR [#81](https://github.com/tiangolo/uwsgi-nginx-docker/pull/81).

## 1.3.0

* This is the last version to support:
    * Debian Stretch (before upgrading to Buster).
    * Python 3.5.
    * Alpine 3.7, 3.8, 3.9 (before upgrading to Alpine 3.11).
    * Alpine in older versions of Python, 2.7 and 3.6 (Before upgrading to Python 3.8).
    * If you need any of those, make sure to use a tag for the build date `2020-05-04`.
* Refactor build set up:
    * Re-use code and configs.
    * Migrate to GitHub Actions.
    * Simplify tests.
    * PR [#78](https://github.com/tiangolo/uwsgi-nginx-docker/pull/78).
* Migrate Travis to .com, update badge. PR [#77](https://github.com/tiangolo/uwsgi-nginx-docker/pull/77).

## 1.2.0

* 2019-10-14:
    * Refactor and simplify test scripts. PR [#66](https://github.com/tiangolo/uwsgi-nginx-docker/pull/66).
* 2019-09-28:
    * Refactor build scripts and add image tags for each build date, like `tiangolo/uwsgi-nginx:python3.7-2019-09-28`. PR [#65](https://github.com/tiangolo/uwsgi-nginx-docker/pull/65).

* Upgrade Travis. PR [#60](https://github.com/tiangolo/uwsgi-nginx-docker/pull/60).

## 1.1.0

* Added support for `/app/prestart.sh` script to run arbitrary code before starting the app (for example, Alembic - SQLAlchemy migrations). The [documentation for the `/app/prestart.sh` is in the main README](https://github.com/tiangolo/uwsgi-nginx-docker#custom-appprestartsh). [PR #59](https://github.com/tiangolo/uwsgi-nginx-docker/pull/59).

## 1.0.0

* 2019-05-04:
    * Add Alpine Linux 3.9. PR [#55](https://github.com/tiangolo/uwsgi-nginx-docker/pull/55) by [evilgoldfish](https://github.com/evilgoldfish).
    * Build images using Travis matrix to improve development/testing speed. Needed for some recent PRs. [PR #58](https://github.com/tiangolo/uwsgi-nginx-docker/pull/58).

* 2019-02-02:
    * The Nginx configurations are generated dynamically from the entrypoint, instead of modifying pre-existing files. [PR #50](https://github.com/tiangolo/uwsgi-nginx-docker/pull/50).
    * Support for a completely custom `/app/nginx.conf` file that overrides the generated one. [PR #51](https://github.com/tiangolo/uwsgi-nginx-docker/pull/51).

* 2018-11-23: New Alpine 3.8 images for Python 2.7, Python 3.6 and Python 3.7 (Python 3.7 temporarily disabled). Thanks to [philippfreyer](https://github.com/philippfreyer) in [PR #45](https://github.com/tiangolo/uwsgi-nginx-docker/pull/45)

* 2018-09-22: New Python 3.7 versions, standard and Alpine based. Thanks to [desaintmartin](https://github.com/desaintmartin) in [this PR](https://github.com/tiangolo/uwsgi-nginx-docker/pull/39).

* 2018-06-22: You can now use `NGINX_WORKER_CONNECTIONS` to set the maximum number of Nginx worker connections and `NGINX_WORKER_OPEN_FILES` to set the maximum number of open files. Thanks to [ronlut](https://github.com/ronlut) in [this PR](https://github.com/tiangolo/uwsgi-nginx-docker/pull/26).

* 2018-06-22: Make uWSGI require an app to run, instead of going in "full dynamic mode" while there was an error. Supervisord doesn't terminate itself but tries to restart uWSGI and shows the errors. Uses `need-app` as suggested by [luckydonald](https://github.com/luckydonald) in [this comment](https://github.com/tiangolo/uwsgi-nginx-flask-docker/issues/3#issuecomment-321991279).

* 2018-06-22: Correctly handled graceful shutdown of uWSGI and Nginx. Thanks to [desaintmartin](https://github.com/desaintmartin) in [this PR](https://github.com/tiangolo/uwsgi-nginx-docker/pull/30).

* 2018-02-04: It's now possible to set the number of Nginx worker processes with the environment variable `NGINX_WORKER_PROCESSES`. Thanks to [naktinis](https://github.com/naktinis) in [this PR](https://github.com/tiangolo/uwsgi-nginx-docker/pull/22).

* 2018-01-14: There are now two Alpine based versions, `python2.7-alpine3.7` and `python3.6-alpine3.7`.

* 2017-12-08: Now you can configure which port the container should listen on, using the environment variable `LISTEN_PORT` thanks to [tmshn](https://github.com/tmshn) in [this PR](https://github.com/tiangolo/uwsgi-nginx-docker/pull/16).

* 2017-08-09: You can set a custom maximum upload file size using an environment variable `NGINX_MAX_UPLOAD`, by default it has a value of `0`, that allows unlimited upload file sizes. This differs from Nginx's default value of 1 MB. It's configured this way because that's the simplest experience a developer that is not expert in Nginx would expect.

* 2017-08-09: Now you can override where to look for the `uwsgi.ini` file, and with that, change the default directory from `/app` to something else, using the envirnoment variable `UWSGI_INI`.

* 2017-08-08: There's a new `latest` tag image, just to show a warning for those still using `latest` for Python 2.7 web applications. As of now, [everyone](https://www.python.org/dev/peps/pep-0373/) [should be](http://flask.pocoo.org/docs/0.12/python3/#python3-support) [using Python 3](https://docs.djangoproject.com/en/1.11/faq/install/#what-python-version-should-i-use-with-django).

* 2017-08-08: Supervisord now terminates uWSGI on `SIGTERM`, so if you run `docker stop` or something similar, it will actually stop everything, instead of waiting for Docker's timeout to kill the container.

* 2017-07-31: There's now an image tag for Python 3.6, based on the official image for Python 3.6 thanks to [jrd](https://github.com/jrd) in [this PR](https://github.com/tiangolo/uwsgi-nginx-docker/pull/6).

* 2016-10-01: Now you can override default `uwsgi.ini` parameters from the file in `/app/uwsgi.ini`.

* 2016-08-16: There's now an image tag for Python 3.5, based on the official image for Python 3.5. So now you can use this image for your projects in Python 2.7 and Python 3.5.

* 2016-08-16: Use dynamic a number of worker processes for uWSGI, from 2 to 16 depending on load. This should work for most cases. This helps especially when there are some responses that are slow and take some time to be generated, this change allows all the other responses to keep fast (in a new process) without having to wait for the first (slow) one to finish.

* Also, it now uses a base `uwsgi.ini` file under `/etc/uwsgi/` with most of the general configurations, so, the `uwsgi.ini` inside `/app` (the one you could need to modify) is now a lot simpler.

* 2016-04-05: Nginx and uWSGI logs are now redirected to stdout, allowing to use `docker logs`.
