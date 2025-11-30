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

<div id="dang-ra" style="margin-top: 50px;"></div>
## 🔥 Truyện Đang Ra
<ul>
  {% for p in site.pages %}
    {% if p.tags contains 'DangRa' %}
      <li><a href="{{ p.url | relative_url }}">{{ p.title }}</a></li>
    {% endif %}
  {% endfor %}
</ul>

<hr>

<div id="hoan-thanh" style="margin-top: 50px;"></div>
## ✅ Hoàn Thành
<ul>
  {% for p in site.pages %}
    {% if p.tags contains 'HoanThanh' %}
      <li><a href="{{ p.url | relative_url }}">{{ p.title }}</a></li>
    {% endif %}
  {% endfor %}
</ul>

<hr>

<div id="drop" style="margin-top: 50px;"></div>
## 🍂 Drop (Hố sâu không đáy)
<ul>
  {% for p in site.pages %}
    {% if p.tags contains 'Drop' %}
      <li><a href="{{ p.url | relative_url }}">{{ p.title }}</a></li>
    {% endif %}
  {% endfor %}
</ul>