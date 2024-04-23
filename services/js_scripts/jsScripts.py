GET_HREFS_SCRIPT = """
        var links = [];
        var items = document.querySelectorAll("li[data-test^='store-item'] a");
        items.forEach(function(item) {
            links.push(item.getAttribute('href'));
        });
        return links;
        """
