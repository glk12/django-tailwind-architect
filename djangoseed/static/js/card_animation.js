document.addEventListener('DOMContentLoaded', () => {
	const observer = new IntersectionObserver((entries) => {
		entries.forEach(entry => {
			if (entry.isIntersecting) {
				entry.target.classList.add('visible');
			} else {
				entry.target.classList.remove('visible');
			}
		});
	}, {
		threshold: 0.1,
		rootMargin: '0px 0px -50px 0px'
	});

	document.querySelectorAll('.fade-in-section, .stagger-fade').forEach(el => {
		observer.observe(el);
	});

	const serviceCards = Array.from(document.querySelectorAll('.service-card'));
	const serviceCardRatios = new Map(serviceCards.map(card => [card, 0]));

	const updateActiveServiceCard = () => {
		const isMobile = window.matchMedia('(max-width: 1023px)').matches;

		if (!isMobile) {
			serviceCards.forEach(card => card.classList.remove('in-view'));
			return;
		}

		let activeCard = null;
		let bestDistanceToCenter = Infinity;
		const viewportHeight = window.innerHeight;
		const viewportCenter = viewportHeight * 0.5;
		const focusStart = viewportHeight * 0.35;
		const focusEnd = viewportHeight * 0.75;

		serviceCards.forEach(card => {
			const ratio = serviceCardRatios.get(card) || 0;
			const rect = card.getBoundingClientRect();
			const cardCenter = rect.top + (rect.height / 2);
			const isInFocusBand = cardCenter >= focusStart && cardCenter <= focusEnd;
			const distanceToCenter = Math.abs(cardCenter - viewportCenter);

			if (isInFocusBand && ratio > 0.05 && distanceToCenter < bestDistanceToCenter) {
				bestDistanceToCenter = distanceToCenter;
				activeCard = card;
			}
		});

		serviceCards.forEach(card => {
			card.classList.toggle('in-view', card === activeCard);
		});
	};

	const serviceCardObserver = new IntersectionObserver((entries) => {
		entries.forEach(entry => {
			serviceCardRatios.set(entry.target, entry.isIntersecting ? entry.intersectionRatio : 0);
		});

		updateActiveServiceCard();
	}, {
		threshold: [0, 0.08, 0.2, 0.35, 0.5, 0.7, 1],
		rootMargin: '0px 0px -8% 0px'
	});

	serviceCards.forEach(card => {
		serviceCardObserver.observe(card);
	});

	window.addEventListener('scroll', updateActiveServiceCard, { passive: true });
	window.addEventListener('resize', updateActiveServiceCard);
});
