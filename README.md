Dibuat oleh Dzaki Gastiadirrijal 122140030 untuk Tugas 1 Pemrograman Web Lanjut
Microservice ini dibuat dari aplikasi Monolith yang dibuat oleh shyam999 :  https://github.com/shyam999/Django-ecommerce 



# Django E-commerce Microservices

Aplikasi berbasis microservices Django e-commerce platform dengan layanan:
1. **Cart Service** - 
2. **Order Service** - 
3. **Coupons Service** -
4. **Shop Service** -

## Setup

1. Clone repository:
    ```bash
    git clone https://github.com/yourusername/Django-ecommerce-microservices.git
    cd Django-ecommerce-microservices
    ```

2. Set up service (Cart, Order, Coupons, Shop) masing masing:
    - untuk setiap layanan, buat virtual environment:
      ```bash
      python -m venv venv
      source venv/bin/activate
      ```

    - Install dependencies:
      ```bash
      pip install -r requirements.txt
      ```

    - Run migrations untuk setiap layanan:
      ```bash
      python manage.py migrate
      ```

3. Pastikan MySQL databases set up:
    - `cart_db`
    - `order_db`
    - `coupons_db`
    - `shop_db`

4. Run each service:
    ```bash
    python manage.py runserver
    ```

5. Use the API Gateway (Nginx) untuk merute request setiap layanan.
