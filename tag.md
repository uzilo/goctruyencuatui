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

<hr>

<div id="dang-ra"></div>
## 🔥 Truyện Đang Ra
<ul>
  {% for p in site.pages %}
    {% if p.tags contains 'DangRa' %}
      <li><a href="{{ p.url | relative_url }}">{{ p.title }}</a></li>
    {% endif %}
  {% endfor %}
</ul>

<hr>

<div id="hoan-thanh"></div>
## ✅ Hoàn Thành
<ul>
  {% for p in site.pages %}
    {% if p.tags contains 'HoanThanh' %}
      <li><a href="{{ p.url | relative_url }}">{{ p.title }}</a></li>
    {% endif %}
  {% endfor %}
</ul>

<hr>

<div id="drop"></div>
## 🍂 Drop (Hố sâu không đáy)
<ul>
  {% for p in site.pages %}
    {% if p.tags contains 'Drop' %}
      <li><a href="{{ p.url | relative_url }}">{{ p.title }}</a></li>
    {% endif %}
  {% endfor %}
</ul>
