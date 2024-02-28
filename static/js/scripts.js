function subscribe(event) {
	event.preventDefault();
	let email = document.getElementById('email-input').value;
	let subscribedEmails = JSON.parse(localStorage.getItem('subscribedEmails')) || [];

	if (subscribedEmails.includes(email)) {
		displayNotification('You have already subscribed. Please enter a different email address.');
		return;
	}

	// Check if email is valid
	let emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
	if (!emailRegex.test(email)) {
		displayNotification('Please enter a valid email address.');
		return;
	}

	// Simulate subscription
	setTimeout(() => {
		displayNotification('You have successfully subscribed!', true);
		subscribedEmails.push(email);
		localStorage.setItem('subscribedEmails', JSON.stringify(subscribedEmails));
	}, 1000);
}

function displayNotification(message, success = false) {
	let notificationDiv = document.getElementById('notification');
	let icon = success ? '<i class="fas fa-check-circle" style="color: #008000;"></i>' : '<i class="fas fa-times-circle" style="color: #FF0000;"></i>';
	let alertClass = success ? 'alert-success' : 'alert-danger';
	
	notificationDiv.innerHTML = `<div class="alert ${alertClass}" style="background-color: #f2f2f2; color: #333; border: 1px solid #ddd; border-radius: 4px; padding: 15px; margin-bottom: 20px;">
									${icon}
									<span style="margin-left: 10px;">${message}</span>
								</div>`;
}

