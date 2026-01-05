(anchors, filters) => {
        return anchors
                .map(anchor => anchor.href)
                .filter(src => filters.some(filter => new RegExp(filter.replace('.', '\\.'), 'i').test(src)));
        }