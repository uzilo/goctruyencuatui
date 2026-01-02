---
layout: default
title: Thể loại
permalink: /tags/
---

<div style="text-align: center; margin-bottom: 40px;">
    <h1 style="color: #2c3e50; font-weight: 800; font-size: 2.2rem; margin-bottom: 10px;">📚 Thể Loại Truyện</h1>
    <p style="color: #7f8c8d; font-size: 1.1rem; max-width: 700px; margin: 0 auto;">
        Khám phá các thể loại truyện theo sở thích của bạn
    </p>
</div>

<div id="dang-ra"></div>
<div style="display: flex; align-items: center; margin-bottom: 20px;">
    <h2 style="margin: 0; color: #e74c3c; font-weight: 700;">🔥 Truyện Đang Ra</h2>
    <div style="flex-grow: 1; height: 1px; background: #eee; margin-left: 20px;"></div>
</div>
<div class="bookshelf-grid">
  {% for p in site.pages %}
    {% if p.tags contains 'DangRa' %}
      <a href="{{ p.url | relative_url }}" class="book-card">
        <img src="{{ p.cover_image }}" alt="{{ p.title }}" class="card-cover" loading="lazy" onerror="this.src='https://placehold.co/200x300?text=No+Cover'">
        <div class="card-body">
            <h3 class="card-title">{{ p.title }}</h3>
            <div class="card-author">Tác giả: {{ p.author }}</div>
            <span class="card-tag" style="background: #ffebee; color: #e74c3c;">{{ p.genres }}</span>
        </div>
      </a>
    {% endif %}
  {% endfor %}
</div>

<hr style="margin: 40px 0; border: 0; border-top: 1px solid #eee;">

<div id="hoan-thanh"></div>
<div style="display: flex; align-items: center; margin-bottom: 20px;">
    <h2 style="margin: 0; color: #27ae60; font-weight: 700;">✅ Hoàn Thành</h2>
    <div style="flex-grow: 1; height: 1px; background: #eee; margin-left: 20px;"></div>
</div>
<div class="bookshelf-grid">
  {% for p in site.pages %}
    {% if p.tags contains 'HoanThanh' %}
      <a href="{{ p.url | relative_url }}" class="book-card" style="border: 2px solid #27ae60;">
        <img src="{{ p.cover_image }}" alt="{{ p.title }}" class="card-cover" loading="lazy" onerror="this.src='https://placehold.co/200x300?text=No+Cover'">
        <div class="card-body">
            <h3 class="card-title" style="color: #27ae60;">{{ p.title }}</h3>
            <div class="card-author">Tác giả: {{ p.author }}</div>
            <span class="card-tag" style="background: #e8f8f5; color: #27ae60;">{{ p.genres }}</span>
        </div>
      </a>
    {% endif %}
  {% endfor %}
</div>

<hr style="margin: 40px 0; border: 0; border-top: 1px solid #eee;">

<div id="drop"></div>
<div style="display: flex; align-items: center; margin-bottom: 20px;">
    <h2 style="margin: 0; color: #95a5a6; font-weight: 700;">🍂 Drop (Hố sâu không đáy)</h2>
    <div style="flex-grow: 1; height: 1px; background: #eee; margin-left: 20px;"></div>
</div>
<div class="bookshelf-grid">
  {% for p in site.pages %}
    {% if p.tags contains 'Drop' %}
      <a href="{{ p.url | relative_url }}" class="book-card" style="opacity: 0.7; border: 1px dashed #95a5a6;">
        <img src="{{ p.cover_image }}" alt="{{ p.title }}" class="card-cover" loading="lazy" onerror="this.src='https://placehold.co/200x300?text=No+Cover'">
        <div class="card-body">
            <h3 class="card-title" style="color: #95a5a6;">{{ p.title }}</h3>
            <div class="card-author">Tác giả: {{ p.author }}</div>
            <span class="card-tag" style="background: #ecf0f1; color: #95a5a6;">{{ p.genres }}</span>
        </div>
      </a>
    {% endif %}
  {% endfor %}
</div>

<hr style="margin: 40px 0; border: 0; border-top: 1px solid #eee;">

<div id="mystery"></div>
<div style="display: flex; align-items: center; margin-bottom: 20px;">
    <h2 style="margin: 0; color: #8e44ad; font-weight: 700;">🕵️ Mystery</h2>
    <div style="flex-grow: 1; height: 1px; background: #eee; margin-left: 20px;"></div>
</div>
<div class="bookshelf-grid">
  {% for p in site.pages %}
    {% if p.tags contains 'Mystery' %}
      <a href="{{ p.url | relative_url }}" class="book-card">
        <img src="{{ p.cover_image }}" alt="{{ p.title }}" class="card-cover" loading="lazy" onerror="this.src='https://placehold.co/200x300?text=No+Cover'">
        <div class="card-body">
            <h3 class="card-title" style="color: #8e44ad;">{{ p.title }}</h3>
            <div class="card-author">Tác giả: {{ p.author }}</div>
            <span class="card-tag" style="background: #f5eef8; color: #8e44ad;">{{ p.genres }}</span>
        </div>
      </a>
    {% endif %}
  {% endfor %}
</div>

<hr style="margin: 40px 0; border: 0; border-top: 1px solid #eee;">

<div id="mm-romance"></div>
<div style="display: flex; align-items: center; margin-bottom: 20px;">
    <h2 style="margin: 0; color: #e91e63; font-weight: 700;">👬 MM Romance</h2>
    <div style="flex-grow: 1; height: 1px; background: #eee; margin-left: 20px;"></div>
</div>
<div class="bookshelf-grid">
  {% for p in site.pages %}
    {% if p.tags contains 'MM Romance' %}
      <a href="{{ p.url | relative_url }}" class="book-card">
        <img src="{{ p.cover_image }}" alt="{{ p.title }}" class="card-cover" loading="lazy" onerror="this.src='https://placehold.co/200x300?text=No+Cover'">
        <div class="card-body">
            <h3 class="card-title" style="color: #e91e63;">{{ p.title }}</h3>
            <div class="card-author">Tác giả: {{ p.author }}</div>
            <span class="card-tag" style="background: #fce4ec; color: #e91e63;">{{ p.genres }}</span>
        </div>
      </a>
    {% endif %}
  {% endfor %}
</div>

<hr style="margin: 40px 0; border: 0; border-top: 1px solid #eee;">

<div id="fantasy"></div>
<div style="display: flex; align-items: center; margin-bottom: 20px;">
    <h2 style="margin: 0; color: #3498db; font-weight: 700;">🧙 Fantasy</h2>
    <div style="flex-grow: 1; height: 1px; background: #eee; margin-left: 20px;"></div>
</div>
<div class="bookshelf-grid">
  {% for p in site.pages %}
    {% if p.tags contains 'Fantasy' %}
      <a href="{{ p.url | relative_url }}" class="book-card">
        <img src="{{ p.cover_image }}" alt="{{ p.title }}" class="card-cover" loading="lazy" onerror="this.src='https://placehold.co/200x300?text=No+Cover'">
        <div class="card-body">
            <h3 class="card-title" style="color: #3498db;">{{ p.title }}</h3>
            <div class="card-author">Tác giả: {{ p.author }}</div>
            <span class="card-tag" style="background: #ebf5fb; color: #3498db;">{{ p.genres }}</span>
        </div>
      </a>
    {% endif %}
  {% endfor %}
</div>

<hr style="margin: 40px 0; border: 0; border-top: 1px solid #eee;">
<p style="text-align: center; color: #999; font-style: italic;">Web này chạy bằng cơm và sự đam mê của TrieuLM.</p>