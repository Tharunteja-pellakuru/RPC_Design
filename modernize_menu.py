import glob
import re

files = glob.glob(r'c:\Users\Desktop\RPC\*.html')

overlay_html = """<!-- Mobile Menu Overlay -->
<div id="mobile-menu" class="fixed inset-0 w-full h-[100dvh] bg-[#faf9f7]/95 dark:bg-[#021526]/95 backdrop-blur-2xl z-[105] hidden flex-col items-center justify-center opacity-0 transition-opacity duration-300">
    <div class="flex flex-col items-center justify-center w-full h-full gap-6 md:gap-8 overflow-y-auto py-24 px-6 relative">
        <a class="nav-mobile-link opacity-0 translate-y-8 text-[#00113a] dark:text-[#faf9f7] font-headline text-4xl sm:text-5xl md:text-6xl tracking-tight transition-all duration-500 hover:-translate-y-1 hover:text-secondary" href="index.html">Home</a>
        <a class="nav-mobile-link opacity-0 translate-y-8 text-[#00113a] dark:text-[#faf9f7] font-headline text-4xl sm:text-5xl md:text-6xl tracking-tight transition-all duration-500 hover:-translate-y-1 hover:text-secondary" href="about.html">About Us</a>
        <a class="nav-mobile-link opacity-0 translate-y-8 text-[#00113a] dark:text-[#faf9f7] font-headline text-4xl sm:text-5xl md:text-6xl tracking-tight transition-all duration-500 hover:-translate-y-1 hover:text-secondary" href="testimonials.html">Testimonials</a>
        <a class="nav-mobile-link opacity-0 translate-y-8 text-[#00113a] dark:text-[#faf9f7] font-headline text-4xl sm:text-5xl md:text-6xl tracking-tight transition-all duration-500 hover:-translate-y-1 hover:text-secondary" href="events.html">Events</a>
        <a class="nav-mobile-link opacity-0 translate-y-8 text-[#00113a] dark:text-[#faf9f7] font-headline text-4xl sm:text-5xl md:text-6xl tracking-tight transition-all duration-500 hover:-translate-y-1 hover:text-secondary" href="gallery.html">Gallery</a>
        <a class="nav-mobile-link opacity-0 translate-y-8 text-[#00113a] dark:text-[#faf9f7] font-headline text-4xl sm:text-5xl md:text-6xl tracking-tight transition-all duration-500 hover:-translate-y-1 hover:text-secondary" href="q&a.html">Q&amp;A</a>
        <a href="contact.html" class="nav-mobile-link opacity-0 translate-y-8 mt-6 md:mt-10 transition-all duration-500">
            <button class="bg-primary text-on-primary px-10 py-4 rounded-full font-label uppercase tracking-widest text-xs md:text-sm hover:bg-primary-container hover:text-white transition-all transform hover:scale-105 shadow-xl">Contact Us</button>
        </a>
    </div>
</div>
</nav>"""

new_script_logic = """// Mobile Menu Logic
  const mobileMenuBtn = document.getElementById('mobile-menu-btn');
  const mobileMenu = document.getElementById('mobile-menu');
  const menuIcon = mobileMenuBtn ? mobileMenuBtn.querySelector('span') : null;
  const mobileLinks = document.querySelectorAll('.nav-mobile-link');
  
  // Set Active Mobile Link
  const currentPath = window.location.pathname.split('/').pop() || 'index.html';
  mobileLinks.forEach(link => {
      if (link.getAttribute('href') === currentPath) {
          link.classList.add('text-secondary', 'dark:text-secondary', 'italic');
          link.classList.remove('text-[#00113a]', 'dark:text-[#faf9f7]');
      }
  });

  if (mobileMenuBtn && mobileMenu && menuIcon) {
      mobileMenuBtn.addEventListener('click', () => {
          const isOpen = !mobileMenu.classList.contains('hidden');
          if (isOpen) {
              // Close menu
              mobileLinks.forEach(link => {
                  link.classList.add('opacity-0', 'translate-y-8');
                  link.classList.remove('translate-y-0', 'opacity-100');
              });
              mobileMenu.classList.add('opacity-0');
              setTimeout(() => { 
                  mobileMenu.classList.add('hidden');
                  mobileMenu.classList.remove('flex');
              }, 300);
              menuIcon.textContent = 'menu';
              document.body.style.overflow = '';
              if (typeof updateNav === 'function') updateNav(); // Re-trigger scroll calculation
          } else {
              // Open menu
              mobileMenu.classList.remove('hidden');
              mobileMenu.classList.add('flex');
              setTimeout(() => { 
                  mobileMenu.classList.remove('opacity-0'); 
                  // Staggered animation
                  mobileLinks.forEach((link, idx) => {
                      setTimeout(() => {
                          link.classList.remove('opacity-0', 'translate-y-8');
                          link.classList.add('opacity-100', 'translate-y-0');
                      }, 100 + (idx * 50));
                  });
              }, 10);
              menuIcon.textContent = 'close';
              document.body.style.overflow = 'hidden';
              if (typeof nav !== 'undefined' && nav) {
                  nav.classList.add('bg-[#faf9f7]', 'dark:bg-[#021526]', 'shadow-sm', 'shadow-[#00113a]/5', 'backdrop-blur-md');
                  nav.classList.remove('bg-transparent', 'nav-transparent');
              }
          }
      });
  }"""

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace overlay
    pattern_overlay = r"<!-- Mobile Menu Overlay -->.*?</div>\s*</nav>"
    content = re.sub(pattern_overlay, overlay_html, content, flags=re.DOTALL)
    
    # Replace Script
    pattern_script = r"// Mobile Menu Logic.*?}\s*\}\);\s*\}"
    if re.search(pattern_script, content, flags=re.DOTALL):
        content = re.sub(pattern_script, new_script_logic, content, flags=re.DOTALL)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
        print("Updated " + f)
