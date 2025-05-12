(function() {
  const data = {
    url: window.location.href
  };

  fetch('https://your-api.com/pageviews/log/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  }).catch(err => {
    console.error('Pageview tracking failed:', err);
  });
})();
