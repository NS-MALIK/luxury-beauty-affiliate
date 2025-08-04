# src/routes/subscription.py

from flask import Blueprint, request, jsonify
from src.models.user import db
from src.models.subscription import Subscriber
from email_validator import validate_email, EmailNotValidError

subscription_bp = Blueprint('subscription', __name__)

@subscription_bp.route('/api/subscribe', methods=['POST'])
def subscribe_email():
    try:
        data = request.get_json()
        email = data.get('email')

        # Server-side email validation
        if not email:
            return jsonify({'success': False, 'message': 'Email address is required.'}), 400
        
        try:
            # Use a robust library for validation
            validate_email(email)
        except EmailNotValidError as e:
            return jsonify({'success': False, 'message': str(e)}), 400

        # Check if the email already exists
        existing_subscriber = Subscriber.query.filter_by(email=email).first()
        if existing_subscriber:
            return jsonify({'success': False, 'message': 'This email is already subscribed.'}), 409

        # Add new subscriber to the database
        new_subscriber = Subscriber(email=email)
        db.session.add(new_subscriber)
        db.session.commit()

        return jsonify({'success': True, 'message': 'You have been successfully subscribed!'}), 201

    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'success': False, 'message': 'An unexpected error occurred.'}), 500


