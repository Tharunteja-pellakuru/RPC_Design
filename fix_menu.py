import os
import glob
import re

files = glob.glob(r'c:\Users\Desktop\RPC\*.html')

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Fix the hamburger menu button classes
    content = content.replace(
        '<button id="mobile-menu-btn" class="nav-btn relative z-[110] md:hidden text-[#00113a] dark:text-[#faf9f7] hover:text-[#735a32] transition-colors p-1 border-transparent border rounded-md">',
        '<button id="mobile-menu-btn" class="nav-link relative z-[110] md:hidden text-[#00113a] dark:text-[#faf9f7] hover:text-[#735a32] transition-colors p-1">'
    )
    
    # We will use regex to find the Mobile Menu Logic section and replace it.
    pattern = r"// Mobile Menu Logic.*?}\s*\}\);\s*\}"
    
    new_script_logic = """// Mobile Menu Logic
  const mobileMenuBtn = document.getElementById('mobile-menu-btn');
  const mobileMenu = document.getElementById('mobile-menu');
  const menuIcon = mobileMenuBtn ? mobileMenuBtn.querySelector('span') : null;

  if (mobileMenuBtn && mobileMenu && menuIcon) {
      mobileMenuBtn.addEventListener('click', () => {
          const isOpen = !mobileMenu.classList.contains('hidden');
          if (isOpen) {
              mobileMenu.classList.add('opacity-0');
              setTimeout(() => { mobileMenu.classList.add('hidden'); }, 300);
              menuIcon.textContent = 'menu';
              document.body.style.overflow = '';
              if (typeof updateNav === 'function') updateNav(); // Re-trigger scroll calculation
          } else {
              mobileMenu.classList.remove('hidden');
              setTimeout(() => { mobileMenu.classList.remove('opacity-0'); }, 10);
              menuIcon.textContent = 'close';
              document.body.style.overflow = 'hidden';
              if (typeof nav !== 'undefined' && nav) {
                  nav.classList.add('bg-[#faf9f7]', 'dark:bg-[#021526]', 'shadow-sm', 'shadow-[#00113a]/5', 'backdrop-blur-md');
                  nav.classList.remove('bg-transparent', 'nav-transparent');
              }
          }
      });
  }"""
    
    content = re.sub(pattern, new_script_logic, content, flags=re.DOTALL)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print("Updated menu behavior in all files.")
