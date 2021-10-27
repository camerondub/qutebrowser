config.load_autoconfig(False)
c.bindings.key_mappings = {'<Ctrl-[>': '<Escape>', '<Ctrl-6>': '<Ctrl-^>', '<Ctrl-M>': '<Return>', '<Ctrl-J>': '<Return>', '<Shift-Return>': '<Return>', '<Enter>': '<Return>', '<Shift-Enter>': '<Return>', '<Ctrl-Enter>': '<Ctrl-Return>'}
c.downloads.location.directory = 'C:/dl'
c.downloads.location.prompt = False
c.downloads.remove_finished = 1000
c.url.default_page = 'file:///C:/opt/qutebrowser/blank.html'
c.url.searchengines = {
	'DEFAULT': 'https://www.google.com/search?q={}',
	'ddg': 'https://duckduckgo.com/?q={}',
	'google': 'https://www.google.com/search?q={}',
	's-3yr': 'https://www.google.com/search?q={}&tbs=qdr:m36',
	's-2yr': 'https://www.google.com/search?q={}&tbs=qdr:m24',
	's-yr': 'https://www.google.com/search?q={}&tbs=qdr:y',
	's-m': 'https://www.google.com/search?q={}&tbs=qdr:m',
	's-w': 'https://www.google.com/search?q={}&tbs=qdr:w',
	's-d': 'https://www.google.com/search?q={}&tbs=qdr:d',
}
c.url.start_pages = ['file:///C:/opt/qutebrowser/blank.html']
c.fonts.default_family = 'Inconsolata-g'
c.fonts.default_size = '11pt'
c.content.pdfjs = True
c.colors.webpage.darkmode.enabled = True
c.colors.webpage.bg = '#191919'
config.bind('<Ctrl-K>', 'scroll-page 0 -1')
config.bind('<Ctrl-J>', 'scroll-page 0 1')
config.bind('<Ctrl-H>', 'scroll-page -1 0')
config.bind('<Ctrl-L>', 'scroll-page 1 0')
config.bind('i', 'mode-enter passthrough')
config.bind('<Alt-Return>', 'fullscreen')
config.bind('<Alt-H>', 'tab-prev') #tab-prev
config.bind('<Alt-J>', 'back') #back
config.bind('<Alt-K>', 'forward') #forward
config.bind('<Alt-L>', 'tab-next') #tab-next
config.bind('<Ctrl-[>', 'mode-leave', mode='passthrough')
config.bind('<Escape>', 'mode-leave', mode='passthrough')
