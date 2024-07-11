echo "DEPLOYING APP"
sudo docker compose down
sudo docker compose up --build -d
sudo docker exec -it workit python manage.py collectstatic --no-input