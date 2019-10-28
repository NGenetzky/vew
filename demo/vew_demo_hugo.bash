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
