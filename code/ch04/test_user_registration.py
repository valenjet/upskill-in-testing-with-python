# test_user_registration.py
import pytest

# Acceptance Test: User Registration Feature
# Given-When-Then format makes requirements clear to all stakeholders

class TestUserRegistration:
    """
    Acceptance tests for user registration feature.
    These tests verify the system meets business requirements.
    """
    
    def test_successful_registration_with_valid_email_and_password(self):
        """
        Scenario: User registers with valid credentials
        Given: A user with valid email and strong password
        When: The user submits the registration form
        Then: The account is created successfully
        And: A welcome email is sent
        """
        # Given
        user_email = "newuser@example.com"
        user_password = "SecurePass123!"
        registration_service = RegistrationService()
        
        # When
        result = registration_service.register_user(
            email=user_email,
            password=user_password
        )
        
        # Then
        assert result.success is True
        assert result.user_id is not None
        assert result.email_sent is True
        assert result.message == "Registration successful"
    
    def test_registration_fails_with_invalid_email_format(self):
        """
        Scenario: User attempts registration with invalid email
        Given: A user with invalid email format
        When: The user submits the registration form
        Then: Registration is rejected
        And: An appropriate error message is shown
        """
        # Given
        invalid_email = "not-an-email"
        user_password = "SecurePass123!"
        registration_service = RegistrationService()
        
        # When
        result = registration_service.register_user(
            email=invalid_email,
            password=user_password
        )
        
        # Then
        assert result.success is False
        assert result.error_code == "INVALID_EMAIL"
        assert "valid email" in result.message.lower()
    
    def test_registration_fails_with_weak_password(self):
        """
        Scenario: User attempts registration with weak password
        Given: A user with valid email but weak password
        When: The user submits the registration form
        Then: Registration is rejected
        And: Password requirements are explained
        """
        # Given
        user_email = "newuser@example.com"
        weak_password = "123"
        registration_service = RegistrationService()
        
        # When
        result = registration_service.register_user(
            email=user_email,
            password=weak_password
        )
        
        # Then
        assert result.success is False
        assert result.error_code == "WEAK_PASSWORD"
        assert "at least 8 characters" in result.message.lower()
    
    def test_registration_fails_when_email_already_exists(self):
        """
        Scenario: User attempts to register with existing email
        Given: An email address already registered in the system
        When: A user tries to register with that email
        Then: Registration is rejected
        And: User is informed email is taken
        """
        # Given
        existing_email = "existing@example.com"
        registration_service = RegistrationService()
        # Pre-register the email
        registration_service.register_user(existing_email, "FirstPass123!")
        
        # When
        result = registration_service.register_user(
            email=existing_email,
            password="SecondPass456!"
        )
        
        # Then
        assert result.success is False
        assert result.error_code == "EMAIL_EXISTS"
        assert "already registered" in result.message.lower()


# Example of the RegistrationService class (system under test)
class RegistrationService:
    """Service for handling user registration."""
    
    def __init__(self):
        self.registered_emails = set()
    
    def register_user(self, email: str, password: str):
        """Register a new user with email and password."""
        # Validate email format
        if "@" not in email or "." not in email:
            return RegistrationResult(
                success=False,
                error_code="INVALID_EMAIL",
                message="Please provide a valid email address"
            )
        
        # Validate password strength
        if len(password) < 8:
            return RegistrationResult(
                success=False,
                error_code="WEAK_PASSWORD",
                message="Password must be at least 8 characters"
            )
        
        # Check if email already exists
        if email in self.registered_emails:
            return RegistrationResult(
                success=False,
                error_code="EMAIL_EXISTS",
                message="Email already registered"
            )
        
        # Register the user
        self.registered_emails.add(email)
        user_id = len(self.registered_emails)
        
        return RegistrationResult(
            success=True,
            user_id=user_id,
            email_sent=True,
            message="Registration successful"
        )


class RegistrationResult:
    """Result object for registration operations."""
    
    def __init__(self, success: bool, user_id: int = None, 
                 email_sent: bool = False, error_code: str = None,
                 message: str = ""):
        self.success = success
        self.user_id = user_id
        self.email_sent = email_sent
        self.error_code = error_code
        self.message = message
