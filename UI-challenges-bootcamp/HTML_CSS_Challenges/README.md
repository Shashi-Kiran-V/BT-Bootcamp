# Personal Learning Dashboard (PLD)

## Framework Chosen
- **Tailwind CSS** (latest CDN version)
- Custom CSS added for hover effects, sticky header, and transitions (~30-40% custom styles)

## Responsive Strategy
- **Mobile-first approach** using Tailwind responsive utilities (`sm:`, `md:`, `lg:` breakpoints)
- Navigation converts to **hamburger menu** on small screens
- Dashboard, Profile, and Gallery cards use **flex and grid** layouts for adaptive content
- All progress bars, modules, and galleries scale according to screen width

## Browser Testing
Tested successfully on:
- **Chrome** ✅
- **Edge** ✅

## Features
1. **Login Page**
   - UI only
   - Mobile-friendly

2. **Dashboard**
   - Topics Explorer: Modules > Units > Topics
   - Labs Tracker: Progress bars with smooth transitions
   - Sticky header with responsive nav
   - Collapsible sections for modules

3. **Profile Page**
   - Display predefined user info
   - Profile image update via icon upload
   - Skills shown as badges
   - Sticky header

4. **Gallery Page**
   - Responsive image grid
   - Hover effects for images
   - Optional modal preview (if added)

5. **Cross-Browser Compatibility**
   - Normalize CSS included
   - No vendor prefixes needed
   - Works across Chrome, Firefox, Safari, and Edge

---

## Folder Notes
- `assets/images/`: Profile image
- `css/`: custom styles (hover, transitions)

