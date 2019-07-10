# Intro

This is my tech blog publishing tool based on
[pelican](https://github.com/getpelican/pelican).

Install [poetry](https://github.com/sdispater/poetry)
as Python virtualenv manager.

To update blogs with pelican:
```
mkdir <my-blog-dir> && cd <my-blog-dir>
git clone git@github.com:leetschau/tech-blog-pelican.git
git clone git@github.com:leetschau/leetschau.github.io.git
git clone git@gitlab.com:leechau/donno-repo.git
git clone https://github.com/getpelican/pelican-plugins.git
git clone https://github.com/getpelican/pelican-themes.git

cd blog_builder
poetry install
alias updateblogs=<my-blog-dir>/blog_builder/updateBlogs.sh
```

Now you can update tech blogs in github.io with `updateblogs`.

BTW: I prefer [q](https://github.com/cal2195/q) to a shell `alias`.
