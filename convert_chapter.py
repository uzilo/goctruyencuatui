import re
import sys

def translate_and_format_chapter(input_file, output_file):
    """
    Read the chapter file and add Vietnamese translations before each English paragraph.
    For now, this creates a template with placeholder Vietnamese text that needs to be filled in.
    """
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to match paragraphs with the old style
    pattern = r'<p style="margin-bottom: 1\.5rem; text-indent: 2em;">(.+?)</p>'
    
    def replace_func(match):
        english_text = match.group(1)
        # Create the new bilingual format
        # Vietnamese placeholder - to be filled in manually
        return f'<p class="lang-vi">[VIETNAMESE TRANSLATION NEEDED]</p>\n<p class="lang-en">{english_text}</p>'
    
    new_content = re.sub(pattern, replace_func, content, flags=re.DOTALL)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Processed {input_file} -> {output_file}")

if __name__ == "__main__":
    if len(sys.argv) >= 3:
        translate_and_format_chapter(sys.argv[1], sys.argv[2])
    else:
        print("Usage: python convert_chapter.py input_file output_file")
