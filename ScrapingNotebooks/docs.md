n elements that contain the provided text.
first – Whether or not to return just the first result.
_encoding – The encoding format.
Example CSS Selectors:

a
a.someClass
a#someID
a[target=_blank]
See W3School’s CSS Selectors Reference for more details.

If first is True, only returns the first Element found.

full_text
The full text content (including links) of the Element or HTML.

html
Unicode representation of the HTML content (learn more).

links
All found links on page, in as–is form.

lxml
lxml representation of the Element or HTML.

next(fetch: bool = False, next_symbol: List[str] = ['next', 'more', 'older']) → Union[requests_html.HTML, List[str]][source]
Attempts to find the next page, if there is one. If fetch is True (default), returns HTML object of next page. If fetch is False, simply returns the next URL.

pq
PyQuery representation of the Element or HTML.

raw_html
Bytes representation of the HTML content. (learn more).

render(retries: int = 8, script: str = None, wait: float = 0.2, scrolldown=False, sleep: int = 0, reload: bool = True, timeout: Union[float, int] = 8.0, keep_page: bool = False, cookies: list = [{}], send_cookies_session: bool = False)[source]
Reloads the response in Chromium, and replaces HTML content with an updated version, with JavaScript executed.

Parameters:	
retries – The number of times to retry loading the page in Chromium.
script – JavaScript to execute upon page load (optional).
wait – The number of seconds to wait before loading the page, preventing timeouts (optional).
scrolldown – Integer, if provided, of how many times to page down.
sleep – Integer, if provided, of how many seconds to sleep after initial render.
reload – If False, content will not be loaded from the browser, but will be provided from memory.
keep_page – If True will allow you to interact with the browser page through r.html.page.
send_cookies_session – If True send HTMLSession.cookies convert.
cookies – If not empty send cookies.
If scrolldown is specified, the page will scrolldown the specified number of times, after sleeping the specified amount of time (e.g. scrolldown=10, sleep=1).

If just sleep is provided, the rendering will wait n seconds, before returning.

If script is specified, it will execute the provided JavaScript at runtime. Example:

script = """
    () => {
        return {
            width: document.documentElement.clientWidth,
            height: document.documentElement.clientHeight,
            deviceScaleFactor: window.devicePixelRatio,
        }
    }
"""
Returns the return value of the executed script, if any is provided:

>>> r.html.render(script=script)
{'width': 800, 'height': 600, 'deviceScaleFactor': 1}
Warning: the first time you run this method, it will download Chromium into your home directory (~/.pyppeteer).

search(template: str) → parse.Result
Search the Element for the given Parse template.

Parameters:	template – The Parse template to use.
search_all(template: str) → Union[List[parse.Result], parse.Result]
Search the Element (multiple times) for the given parse template.

Parameters:	template – The Parse template to use.
text
The text content of the Element or HTML.

xpath(selector: str, *, clean: bool = False, first: bool = False, _encoding: str = None) → Union[List[str], List[requests_html.Element], str, requests_html.Element]
Given an XPath selector, returns a list of Element objects or a single one.

Parameters:	
selector – XPath Selector to use.
clean – Whether or not to sanitize the found HTML of <script> and <style> tags.
first – Whether or not to return just the first result.
_encoding – The encoding format.
If a sub-selector is specified (e.g. //a/@href), a simple list of results is returned.

See W3School’s XPath Examples for more details.

If first is True, only returns the first Element found.

class requests_html.Element(*, element, url: str, default_encoding: str = None)[source]
An element of HTML.

Parameters:	
element – The element from which to base the parsing upon.
url – The URL from which the HTML originated, used for absolute_links.
default_encoding – Which encoding to default to.
absolute_links
All found links on page, in absolute form (learn more).

attrs
Returns a dictionary of the attributes of the Element (learn more).

base_url
The base URL for the page. Supports the <base> tag (learn more).

encoding
The encoding string to be used, extracted from the HTML and HTMLResponse headers.

find(selector: str = '*', *, containing: Union[str, List[str]] = None, clean: bool = False, first: bool = False, _encoding: str = None) → Union[List[requests_html.Element], requests_html.Element]
Given a CSS Selector, returns a list of Element objects or a single one.

Parameters:	
selector – CSS Selector to use.
clean – Whether or not to sanitize the found HTML of <script> and <style> tags.
containing – If specified, only return elements that contain the provided text.
first – Whether or not to return just the first result.
_encoding – The encoding format.
Example CSS Selectors:

a
a.someClass
a#someID
a[target=_blank]
See W3School’s CSS Selectors Reference for more details.

If first is True, only returns the first Element found.

full_text
The full text content (including links) of the Element or HTML.

html
Unicode representation of the HTML content (learn more).

links
All found links on page, in as–is form.

lxml
lxml representation of the Element or HTML.

pq
PyQuery representation of the Element or HTML.

raw_html
Bytes representation of the HTML content. (learn more).

search(template: str) → parse.Result
Search the Element for the given Parse template.

Parameters:	template – The Parse template to use.
search_all(template: str) → Union[List[parse.Result], parse.Result]
Search the Element (multiple times) for the given parse template.

Parameters:	template – The Parse template to use.
text
The text content of the Element or HTML.

xpath(selector: str, *, clean: bool = False, first: bool = False, _encoding: str = None) → Union[List[str], List[requests_html.Element], str, requests_html.Element]
Given an XPath selector, returns a list of Element objects or a single one.

Parameters:	
selector – XPath Selector to use.
clean – Whether or not to sanitize the found HTML of <script> and <style> tags.
first – Whether or not to return just the first result.
_encoding – The encoding format.
If a sub-selector is specified (e.g. //a/@href), a simple list of results is returned.

See W3School’s XPath Examples for more details.

If first is True, only returns the first Element found.

Utility Functions
requests_html.user_agent(style=None) → str[source]
Returns an apparently legit user-agent, if not requested one of a specific style. Defaults to a Chrome-style User-Agent.

HTML Sessions
These sessions are for making HTTP requests:

class requests_html.HTMLSession(**kwargs)[source]
close()[source]
If a browser was created close it first.

delete(url, **kwargs)
Sends a DELETE request. Returns Response object.

Parameters:	
url – URL for the new Request object.
**kwargs – Optional arguments that request takes.
Return type:	
requests.Response

get(url, **kwargs)
Sends a GET request. Returns Response object.

Parameters:	
url – URL for the new Request object.
**kwargs – Optional arguments that request takes.
Return type:	
requests.Response

get_adapter(url)
Returns the appropriate connection adapter for the given URL.

Return type:	requests.adapters.BaseAdapter
get_redirect_target(resp)
Receives a Response. Returns a redirect URI or None

head(url, **kwargs)
Sends a HEAD request. Returns Response object.

Parameters:	
url – URL for the new Request object.
**kwargs – Optional arguments that request takes.
Return type:	
requests.Response

merge_environment_settings(url, proxies, stream, verify, cert)
Check the environment and merge it with some settings.

Return type:	dict
mount(prefix, adapter)
Registers a connection adapter to a prefix.

Adapters are sorted in descending order by prefix length.

options(url, **kwargs)
Sends a OPTIONS request. Returns Response object.

Parameters:	
url – URL for the new Request object.
**kwargs – Optional arguments that request takes.
Return type:	
requests.Response

patch(url, data=None, **kwargs)
Sends a PATCH request. Returns Response object.

Parameters:	
url – URL for the new Request object.
data – (optional) Dictionary, list of tuples, bytes, or file-like object to send in the body of the Request.
**kwargs – Optional arguments that request takes.
Return type:	
requests.Response

post(url, data=None, json=None, **kwargs)
Sends a POST request. Returns Response object.

Parameters:	
url – URL for the new Request object.
data – (optional) Dictionary, list of tuples, bytes, or file-like object to send in the body of the Request.
json – (optional) json to send in the body of the Request.
**kwargs – Optional arguments that request takes.
Return type:	
requests.Response

prepare_request(request)
Constructs a PreparedRequest for transmission and returns it. The PreparedRequest has settings merged from the Request instance and those of the Session.

Parameters:	request – Request instance to prepare with this session’s settings.
Return type:	requests.PreparedRequest
put(url, data=None, **kwargs)
Sends a PUT request. Returns Response object.

Parameters:	
url – URL for the new Request object.
data – (optional) Dictionary, list of tuples, bytes, or file-like object to send in the body of the Request.
**kwargs – Optional arguments that request takes.
Return type:	
requests.Response

rebuild_auth(prepared_request, response)
When being redirected we may want to strip authentication from the request to avoid leaking credentials. This method intelligently removes and reapplies authentication where possible to avoid credential loss.

rebuild_method(prepared_request, response)
When being redirected we may want to change the method of the request based on certain specs or browser behavior.

rebuild_proxies(prepared_request, proxies)
This method re-evaluates the proxy configuration by considering the environment variables. If we are redirected to a URL covered by NO_PROXY, we strip the proxy configuration. Otherwise, we set missing proxy keys for this URL (in case they were stripped by a previous redirect).

This method also replaces the Proxy-Authorization header where necessary.

Return type:	dict
request(method, url, params=None, data=None, headers=None, cookies=None, files=None, auth=None, timeout=None, allow_redirects=True, proxies=None, hooks=None, stream=None, verify=None, cert=None, json=None)
Constructs a Request, prepares it and sends it. Returns Response object.

Parameters:	
method – method for the new Request object.
url – URL for the new Request object.
params – (optional) Dictionary or bytes to be sent in the query string for the Request.
data – (optional) Dictionary, list of tuples, bytes, or file-like object to send in the body of the Request.
json – (optional) json to send in the body of the Request.
headers – (optional) Dictionary of HTTP Headers to send with the Request.
cookies – (optional) Dict or CookieJar object to send with the Request.
files – (optional) Dictionary of 'filename': file-like-objects for multipart encoding upload.
auth – (optional) Auth tuple or callable to enable Basic/Digest/Custom HTTP Auth.
timeout (float or tuple) – (optional) How long to wait for the server to send data before giving up, as a float, or a (connect timeout, read timeout) tuple.
allow_redirects (bool) – (optional) Set to True by default.
proxies – (optional) Dictionary mapping protocol or protocol and hostname to the URL of the proxy.
stream – (optional) whether to immediately download the response content. Defaults to False.
verify – (optional) Either a boolean, in which case it controls whether we verify the server’s TLS certificate, or a string, in which case it must be a path to a CA bundle to use. Defaults to True.
cert – (optional) if String, path to ssl client cert file (.pem). If Tuple, (‘cert’, ‘key’) pair.
Return type:	
requests.Response

resolve_redirects(resp, req, stream=False, timeout=None, verify=True, cert=None, proxies=None, yield_requests=False, **adapter_kwargs)
Receives a Response. Returns a generator of Responses or Requests.

response_hook(response, **kwargs) → requests_html.HTMLResponse
Change response enconding and replace it by a HTMLResponse.

send(request, **kwargs)
Send a given PreparedRequest.

Return type:	requests.Response
should_strip_auth(old_url, new_url)
Decide whether Authorization header should be removed when redirecting

class requests_html.AsyncHTMLSession(loop=None, workers=None, mock_browser: bool = True, *args, **kwargs)[source]
An async consumable session.

close()[source]
If a browser was created close it first.

delete(url, **kwargs)
Sends a DELETE request. Returns Response object.

Parameters:	
url – URL for the new Request object.
**kwargs – Optional arguments that request takes.
Return type:	
requests.Response

get(url, **kwargs)
Sends a GET request. Returns Response object.

Parameters:	
url – URL for the new Request object.
**kwargs – Optional arguments that request takes.
Return type:	
requests.Response

get_adapter(url)
Returns the appropriate connection adapter for the given URL.

Return type:	requests.adapters.BaseAdapter
get_redirect_target(resp)
Receives a Response. Returns a redirect URI or None

head(url, **kwargs)
Sends a HEAD request. Returns Response object.

Parameters:	
url – URL for the new Request object.
**kwargs – Optional arguments that request takes.
Return type:	
requests.Response

merge_environment_settings(url, proxies, stream, verify, cert)
Check the environment and merge it with some settings.

Return type:	dict
mount(prefix, adapter)
Registers a connection adapter to a prefix.

Adapters are sorted in descending order by prefix length.

options(url, **kwargs)
Sends a OPTIONS request. Returns Response object.

Parameters:	
url – URL for the new Request object.
**kwargs – Optional arguments that request takes.
Return type:	
requests.Response

patch(url, data=None, **kwargs)
Sends a PATCH request. Returns Response object.

Parameters:	
url – URL for the new Request object.
data – (optional) Dictionary, list of tuples, bytes, or file-like object to send in the body of the Request.
**kwargs – Optional arguments that request takes.
Return type:	
requests.Response

post(url, data=None, json=None, **kwargs)
Sends a POST request. Returns Response object.

Parameters:	
url – URL for the new Request object.
data – (optional) Dictionary, list of tuples, bytes, or file-like object to send in the body of the Request.
json – (optional) json to send in the body of the Request.
**kwargs – Optional arguments that request takes.
Return type:	
requests.Response

prepare_request(request)
Constructs a PreparedRequest for transmission and returns it. The PreparedRequest has settings merged from the Request instance and those of the Session.

Parameters:	request – Request instance to prepare with this session’s settings.
Return type:	requests.PreparedRequest
put(url, data=None, **kwargs)
Sends a PUT request. Returns Response object.

Parameters:	
url – URL for the new Request object.
data – (optional) Dictionary, list of tuples, bytes, or file-like object to send in the body of the Request.
**kwargs – Optional arguments that request takes.
Return type:	
requests.Response

rebuild_auth(prepared_request, response)
When being redirected we may want to strip authentication from the request to avoid leaking credentials. This method intelligently removes and reapplies authentication where possible to avoid credential loss.

rebuild_method(prepared_request, response)
When being redirected we may want to change the method of the request based on certain specs or browser behavior.

rebuild_proxies(prepared_request, proxies)
This method re-evaluates the proxy configuration by considering the environment variables. If we are redirected to a URL covered by NO_PROXY, we strip the proxy configuration. Otherwise, we set missing proxy keys for this URL (in case they were stripped by a previous redirect).

This method also replaces the Proxy-Authorization header where necessary.

Return type:	dict
request(*args, **kwargs)[source]
Partial original request func and run it in a thread.

resolve_redirects(resp, req, stream=False, timeout=None, verify=True, cert=None, proxies=None, yield_requests=False, **adapter_kwargs)
Receives a Response. Returns a generator of Responses or Requests.

response_hook(response, **kwargs) → requests_html.HTMLResponse
Change response enconding and replace it by a HTMLResponse.

run(*coros)[source]
Pass in all the coroutines you want to run, it will wrap each one in a task, run it and wait for the result. Return a list with all results, this is returned in the same order coros are passed in.

send(request, **kwargs)
Send a given PreparedRequest.

Return type:	requests.Response
should_strip_auth(old_url, new_url)
Decide whether Authorization header should be removed when redirecting