#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to convert chapter files to bilingual format.
This creates a template structure that you can fill in with Vietnamese translations.
"""

import re
import sys

# Dictionary of translations for Chapter 12
# Key: English text (or part of it for matching)
# Value: Vietnamese translation
TRANSLATIONS = {
    "Chapter Twelve": "Chương Mười Hai",
    "Shane was shocked to find it was morning when he opened his eyes": "Shane sốc khi mở mắt ra và thấy trời đã sáng. Cậu không nhớ mình đã ngủ lúc nào, nhưng chắc hẳn đã kiệt sức sau trận đấu và màn ân ái mãnh liệt.",
    "God, and the edging": 'Trời ơi, còn cả màn "kìm nén" nữa. Nóng bỏng vãi chưởng.',
    "He could hear Ilya snoring softly behind him": "Cậu có thể nghe Ilya ngáy nhẹ sau lưng, một cánh tay mạnh mẽ vắt lỏng lẻo qua eo Shane. Shane mỉm cười và ngả người tựa vào anh, thở dài hạnh phúc. Cậu đang cương, và cậu cảm nhận được Ilya cũng vậy, nhưng cậu có thể bỏ qua điều đó bây giờ. Chuyện ấy thì tuyệt rồi, nhưng những khoảnh khắc như thế này, nơi họ có thể ôm ấp, vuốt ve và chỉ đơn giản là tồn tại bên nhau trong một căn phòng yên tĩnh, mới là điều Shane yêu thích nhất.",
    "Shane was normally an early riser": "Shane thường là người dậy sớm, và tuân thủ một thói quen nghiêm ngặt mỗi sáng. Nhưng thay vì nhảy khỏi giường và mặc đồ chạy bộ, sáng nay cậu đã chìm đắm trong sự thoải mái khi được người mình yêu ôm ấp, và thiếp đi.",
    "He was awoken sometime later by Ilya trailing kisses": "Cậu bị đánh thức một lúc sau bởi Ilya rải những nụ hôn dọc theo vai cậu.",
}

def convert_file(input_path, output_path=None):
    """Convert a chapter file to bilingual format."""
    if output_path is None:
        output_path = input_path
    
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to match paragraphs
    pattern = r'<p style="margin-bottom: 1\.5rem; text-indent: 2em;">(.+?)</p>'
    
    def replace_paragraph(match):
        english_text = match.group(1)
        
        # Try to find a translation
        vi_text = None
        for key, value in TRANSLATIONS.items():
            if key in english_text:
                vi_text = value
                break
        
        if vi_text:
            return f'<p class="lang-vi">{vi_text}</p>\n<p class="lang-en">{english_text}</p>'
        else:
            # Keep original if no translation found
            return f'<p class="lang-vi">[NEEDS TRANSLATION]</p>\n<p class="lang-en">{english_text}</p>'
    
    new_content = re.sub(pattern, replace_paragraph, content, flags=re.DOTALL)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Converted: {input_path}")
    if output_path != input_path:
        print(f"Output: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python convert_bilingual.py <chapter_file> [output_file]")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    convert_file(input_file, output_file)
