import os

org_path = r'c:\Users\hiufung_lau\Documents\SELF\LCM\Org\Org.html'
index_path = r'c:\Users\hiufung_lau\Documents\SELF\LCM\index.html'

with open(org_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace hero image
content = content.replace(
    'src="https://images.unsplash.com/photo-1604605801370-3481ed27814b?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80" alt="專業針灸特寫" class="w-full h-full object-cover object-center" />',
    'src="pic/photo1.png" alt="專業針灸特寫" class="w-full h-full object-cover object-center" onerror="this.src=\'https://images.unsplash.com/photo-1604605801370-3481ed27814b?q=80&w=2000\'" />'
)

# Replace service 1
content = content.replace(
    'src="https://images.unsplash.com/photo-1544161515-4ab6ce6db874?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="中醫推拿理療" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700">',
    'src="pic/photo3.png" alt="中醫推拿理療" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700" onerror="this.src=\'https://images.unsplash.com/photo-1544161515-4ab6ce6db874?q=80&w=800\'">'
)

# Replace service 2
content = content.replace(
    'src="https://images.unsplash.com/photo-1552693673-1bf958298935?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="傳統拔罐與針灸" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700">',
    'src="pic/photo2.png" alt="傳統拔罐與針灸" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700" onerror="this.src=\'https://images.unsplash.com/photo-1552693673-1bf958298935?q=80&w=800\'">'
)

# Replace service 3
content = content.replace(
    'src="https://images.unsplash.com/photo-1598514982205-f36b96d1e8d4?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="中醫藥材調理" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700">',
    'src="pic/photo4.png" alt="中醫藥材調理" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700" onerror="this.src=\'https://images.unsplash.com/photo-1598514982205-f36b96d1e8d4?q=80&w=800\'">'
)

# Update the page title to match what was there if necessary? The Org.html title is "劉志明中醫推拿診所 | 旺角專業中醫・告別痛症", which is fine.

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("index.html has been successfully restored with updated image paths!")
