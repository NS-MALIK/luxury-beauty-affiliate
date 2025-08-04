"""
Sample product data for CuratedFinds
Focus on low-competition, high-value products without mentioning competition levels
"""

SAMPLE_CATEGORIES = [
    {
        'name': 'Health & Wellness',
        'slug': 'health-wellness',
        'description': 'Carefully selected health and wellness products for better living',
        'icon': 'heart'
    },
    {
        'name': 'Home & Kitchen',
        'slug': 'home-kitchen',
        'description': 'Essential home and kitchen items that make life easier',
        'icon': 'home'
    },
    {
        'name': 'Baby & Kids',
        'slug': 'baby-kids',
        'description': 'Safe and innovative products for children and babies',
        'icon': 'baby'
    },
    {
        'name': 'Fitness & Sports',
        'slug': 'fitness-sports',
        'description': 'Quality fitness and sports equipment for active lifestyles',
        'icon': 'dumbbell'
    },
    {
        'name': 'Tech & Gadgets',
        'slug': 'tech-gadgets',
        'description': 'Innovative technology and gadgets for modern living',
        'icon': 'smartphone'
    },
    {
        'name': 'Beauty & Personal Care',
        'slug': 'beauty-personal-care',
        'description': 'Premium beauty and personal care essentials',
        'icon': 'sparkles'
    }
]

SAMPLE_PRODUCTS = [
    # Health & Wellness
    {
        'title': 'Ergonomic Lumbar Support Memory Foam Pillow',
        'description': 'Premium memory foam lumbar support pillow designed for perfect spinal alignment. Features breathable bamboo cover and ergonomic design for all-day comfort.',
        'price': 29.99,
        'original_price': 49.99,
        'discount_percentage': 40,
        'amazon_url': 'https://amazon.com/dp/example1',
        'image_url': 'https://images.unsplash.com/photo-1586953208448-b95a79798f07?w=400',
        'category': 'Health & Wellness',
        'rating': 4.7,
        'review_count': 1247,
        'features': ['Memory foam construction', 'Breathable bamboo cover', 'Ergonomic design', 'Machine washable'],
        'tags': ['back support', 'office chair', 'posture', 'comfort'],
        'is_featured': True,
        'is_bestseller': True
    },
    {
        'title': 'Copper-Infused Compression Gloves for Arthritis',
        'description': 'Therapeutic compression gloves infused with copper for natural pain relief. Perfect for arthritis, carpal tunnel, and joint stiffness.',
        'price': 19.95,
        'original_price': 34.95,
        'discount_percentage': 43,
        'amazon_url': 'https://amazon.com/dp/example2',
        'image_url': 'https://images.unsplash.com/photo-1559757148-5c350d0d3c56?w=400',
        'category': 'Health & Wellness',
        'rating': 4.5,
        'review_count': 892,
        'features': ['Copper-infused fabric', 'Graduated compression', 'Breathable material', 'Open finger design'],
        'tags': ['arthritis', 'compression', 'pain relief', 'copper'],
        'is_featured': False,
        'is_bestseller': True
    },
    
    # Home & Kitchen
    {
        'title': 'Bamboo Cutting Board Set with Built-in Compartments',
        'description': 'Sustainable bamboo cutting board with innovative compartment design. Features juice grooves, antimicrobial properties, and easy storage.',
        'price': 34.99,
        'original_price': 59.99,
        'discount_percentage': 42,
        'amazon_url': 'https://amazon.com/dp/example3',
        'image_url': 'https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?w=400',
        'category': 'Home & Kitchen',
        'rating': 4.8,
        'review_count': 2156,
        'features': ['Sustainable bamboo', 'Built-in compartments', 'Juice grooves', 'Antimicrobial surface'],
        'tags': ['bamboo', 'cutting board', 'kitchen', 'sustainable'],
        'is_featured': True,
        'is_bestseller': False
    },
    {
        'title': 'Silicone Stretch Lids Universal Food Covers',
        'description': 'Eco-friendly silicone stretch lids that replace plastic wrap. Set of 6 different sizes fits bowls, cups, and containers perfectly.',
        'price': 12.99,
        'original_price': 24.99,
        'discount_percentage': 48,
        'amazon_url': 'https://amazon.com/dp/example4',
        'image_url': 'https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?w=400',
        'category': 'Home & Kitchen',
        'rating': 4.6,
        'review_count': 1834,
        'features': ['Food-grade silicone', 'Dishwasher safe', 'Microwave safe', 'Reusable'],
        'tags': ['silicone', 'food storage', 'eco-friendly', 'kitchen'],
        'is_featured': False,
        'is_bestseller': True
    },
    
    # Baby & Kids
    {
        'title': 'Sensory Fidget Toys Set for Focus and Calm',
        'description': 'Premium sensory fidget toys designed to improve focus and reduce anxiety. Perfect for kids with ADHD, autism, or stress relief.',
        'price': 16.99,
        'original_price': 29.99,
        'discount_percentage': 43,
        'amazon_url': 'https://amazon.com/dp/example5',
        'image_url': 'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=400',
        'category': 'Baby & Kids',
        'rating': 4.7,
        'review_count': 967,
        'features': ['BPA-free materials', 'Quiet operation', 'Portable design', 'Multiple textures'],
        'tags': ['fidget toys', 'sensory', 'focus', 'stress relief'],
        'is_featured': True,
        'is_bestseller': False
    },
    {
        'title': 'Montessori Wooden Learning Tower for Toddlers',
        'description': 'Adjustable wooden learning tower that grows with your child. Promotes independence and safe kitchen participation.',
        'price': 89.99,
        'original_price': 149.99,
        'discount_percentage': 40,
        'amazon_url': 'https://amazon.com/dp/example6',
        'image_url': 'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=400',
        'category': 'Baby & Kids',
        'rating': 4.9,
        'review_count': 543,
        'features': ['Solid wood construction', 'Adjustable height', 'Safety rails', 'Easy assembly'],
        'tags': ['montessori', 'learning tower', 'toddler', 'kitchen helper'],
        'is_featured': False,
        'is_bestseller': True
    },
    
    # Fitness & Sports
    {
        'title': 'Resistance Loop Bands Set with Door Anchor',
        'description': 'Professional-grade resistance bands with door anchor system. Perfect for home workouts, physical therapy, and strength training.',
        'price': 24.99,
        'original_price': 44.99,
        'discount_percentage': 44,
        'amazon_url': 'https://amazon.com/dp/example7',
        'image_url': 'https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=400',
        'category': 'Fitness & Sports',
        'rating': 4.6,
        'review_count': 1456,
        'features': ['Natural latex material', 'Door anchor included', 'Multiple resistance levels', 'Portable design'],
        'tags': ['resistance bands', 'home workout', 'fitness', 'strength training'],
        'is_featured': True,
        'is_bestseller': True
    },
    
    # Tech & Gadgets
    {
        'title': 'Wireless Phone Charger with Cooling Fan',
        'description': 'Fast wireless charger with built-in cooling fan to prevent overheating. Compatible with all Qi-enabled devices.',
        'price': 22.99,
        'original_price': 39.99,
        'discount_percentage': 43,
        'amazon_url': 'https://amazon.com/dp/example8',
        'image_url': 'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=400',
        'category': 'Tech & Gadgets',
        'rating': 4.5,
        'review_count': 2234,
        'features': ['Fast charging', 'Cooling fan', 'LED indicator', 'Universal compatibility'],
        'tags': ['wireless charger', 'phone accessories', 'fast charging', 'cooling'],
        'is_featured': False,
        'is_bestseller': True
    },
    
    # Beauty & Personal Care
    {
        'title': 'Jade Roller and Gua Sha Set for Face Massage',
        'description': 'Authentic jade facial massage tools for lymphatic drainage and skin rejuvenation. Includes storage pouch and instruction guide.',
        'price': 18.99,
        'original_price': 34.99,
        'discount_percentage': 46,
        'amazon_url': 'https://amazon.com/dp/example9',
        'image_url': 'https://images.unsplash.com/photo-1556228720-195a672e8a03?w=400',
        'category': 'Beauty & Personal Care',
        'rating': 4.4,
        'review_count': 1678,
        'features': ['Authentic jade stone', 'Ergonomic design', 'Storage pouch included', 'Instruction guide'],
        'tags': ['jade roller', 'face massage', 'skincare', 'beauty tools'],
        'is_featured': True,
        'is_bestseller': False
    }
]
