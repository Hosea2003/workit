echo "DEPLOYING APP"
sudo docker compose down
sudo docker compose up --build -d
# collectstatic
# sudo docker exec -it workit python manage.py collectstatic --no-input