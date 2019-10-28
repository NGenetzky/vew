
# vew

The exact meaning of these three letters is still up for debate. These
letters were originally chosen because this package was designed to integrate
with [virtualenvwrapper][virtualenvwrapper_rtd]. To be quite frank, I like
the short name and I am confident that full meaning will evolve naturally.

Possible meanings of the three letters:

- virtual environment wrapper
- virtual environment workspace
- virtually enter world
- virtually enter workspace
- virtual engineer workspace
- virtual encapsulated workspace

## Motvation

Project provides an interface to an encapsulated workspace on which the
following actions can be performed:

- activated, deactivated
- imported, exported, saved, loaded

The secondary motivation is to provide modular/optional integration with
powerful tools such as:

- [hugo-academic][hugo_theme_academic]
- [hugo][]
- [joplin][]
- [papis][papis_rtd]
- [virtualenv][virtualenv_pypi]
- [virtualenvwrapper][virtualenvwrapper_rtd]

## Packages

### vew.hugo

Simple demo script

```bash
#!/bin/bash

# bash strict mode
set -euo pipefail
IFS=$'\n\t'
# demonstration
set -x

vew_demo_hugo(){
    d_demo="${1?d_demo}"
    # Create vew that contains vew.hugo
    mkdir -p "${d_demo}/demo.vew/"
    vew_hugo --root "${d_demo}/demo.vew/" --init

    # Ensure you have the hugo theme
    mkdir -p "${d_demo}/vew-hugo-themes/"
    if [ ! -d "${d_demo}/vew-hugo-themes/academic" ] ; then
        git clone \
            'https://github.com/gcushen/hugo-academic.git' \
            "${d_demo}/vew-hugo-themes/academic"
        (
            cd "${d_demo}/vew-hugo-themes/academic"
            git checkout 'v4.2.5'
        )
    fi

    # Examine contents, and then build and serve website with hugo
    cd "${d_demo}/demo.vew/"
    find './'
    hugo --themesDir '../vew-hugo-themes'
    hugo --themesDir '../vew-hugo-themes' serve
}

vew_demo_hugo './vew-demo-hugo/'

```


## References

- [hugo][]
- [hugo_theme_academic][]
- [joplin][]
- [joplin_py_api][]
- [joplin_rest_api][]
- [papis_rtd][]
- [taskwarrior][]
- [virtualenvwrapper_rtd][]
- [virtualenv_pypi][]


[hugo]: https://gohugo.io/
[hugo_theme_academic]: https://themes.gohugo.io/academic/
[joplin]: https://joplinapp.org
[joplin_py_api]: https://pypi.org/project/joplin-api/
[joplin_rest_api]: https://joplinapp.org/api/
[papis_rtd]: https://papis.readthedocs.io/en/latest/
[taskwarrior]:https://taskwarrior.org/
[virtualenv_pypi]: virtualenv_pypi
[virtualenvwrapper_rtd]: https://virtualenvwrapper.readthedocs.io/en/latest/
