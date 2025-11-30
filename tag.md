---
layout: page
title: Thể loại
permalink: /tags/
---

<div id="mystery"></div>
## 🕵️ Mystery
<ul>
  {% for p in site.pages %}
    {% if p.tags contains 'Mystery' %}
      <li><a href="{{ p.url | relative_url }}">{{ p.title }}</a></li>
    {% endif %}
  {% endfor %}
</ul>

<hr>

<div id="mm-romance"></div>
## 👬 MM
<ul>
  {% for p in site.pages %}
    {% if p.tags contains 'MM Romance' %}
      <li><a href="{{ p.url | relative_url }}">{{ p.title }}</a></li>
    {% endif %}
  {% endfor %}
</ul>

<hr>

<div id="fantasy"></div>
## 🧙 Fantasy
<ul>
  {% for p in site.pages %}
    {% if p.tags contains 'Fantasy' %}
      <li><a href="{{ p.url | relative_url }}">{{ p.title }}</a></li>
    {% endif %}
  {% endfor %}
</ul>