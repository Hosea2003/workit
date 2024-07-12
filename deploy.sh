echo "DEPLOYING APP"
# sudo docker exec -it workit python manage.py collectstatic --no-input
sudo docker compose down
sudo docker compose up --build -d