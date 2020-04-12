# Blog Publisher

This is my tech blog publishing tool based on
[pelican](https://github.com/getpelican/pelican).

## Prerequisites

* [asdf](https://github.com/asdf-vm/asdf)

* Python >= 3.7

* [direnv](https://github.com/direnv/direnv)

* [asdf-direnv](https://github.com/asdf-community/asdf-direnv)

Install asdf first, then install Python, direnv, asdf-direnv with 
asdf. See Readme of asdf-direnv for installation and configuration
of direnv and asdf-direnv.

## Install

```
mkdir <my-blog-dir> && cd <my-blog-dir>
git clone git@github.com:leetschau/tech-blog-pelican.git
git clone git@github.com:leetschau/leetschau.github.io.git
git clone git@gitlab.com:leechau/donno-repo.git
git clone https://github.com/getpelican/pelican-plugins.git
git clone https://github.com/getpelican/pelican-themes.git

cd blog_builder
python -m venv env
. env/bin/activate
pip install -r requirements.txt
```

## Usage

Update tech blogs in github.io with:
```
cd <my-blog-dir>/blog_builder
./updateBlogs.sh
```

After going into the blog_builder folder,
`direnv` load automatically the local Python virtualenv
installed previously according to .envrc file.

