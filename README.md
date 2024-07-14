# restaurant

<!-- {% for category, dishes in category_dishes.items %}
{% for i in range(2) %}
        <h1>Most popular {{ category.name }}{% if category.name == 'Sushi' %} meals{% else %}s{% endif %}</h1>
        <div class="dishes">
            {% for dish in dishes %}
                <div class="dish-card">
                    <img src="{{ dish.image.url }}" alt="{{ dish.name }}">
                    <div class="dish-content">
                        <h2>{{ dish.name }}</h2>
                        <p>
                            ({{ dish.order_count }}
                            {% if dish.order_count == 1 %}order
                            {% else %}orders{% endif %})
                        </p>
                    </div>
                    <p class="silver">{{ dish.description }}</p>
                </div>
            {% endfor %}
        </div>
    {% endfor %}
{% endfor %} -->