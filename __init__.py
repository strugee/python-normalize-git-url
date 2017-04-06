import re
from six.moves.urllib_parse import urlparse, urlunparse

# We compile regexes at module init for performance
protocolGit = re.compile(r'^git\+')
protocolGitHttps = re.compile(r'^git\+https?')
pathnameNotNumbers = re.compile(r'\/?:[^0-9]')
protocolManipulator = re.compile(r'^git\+(.*:[^:]+):(.*)')
protocolGitFile = re.compile(r'^git\+file')
protocolGitSsh = re.compile(r'^(?:git\+)?ssh:\/\/')
urlHash = re.compile('#[^#]*$')

def normalizeGitUrl(u):
    parsed = urlparse(u)

    # If parsing actually alters the URL, it is almost certainly an
    # scp-style URL, or an invalid one.
    altered = u != urlunparse(parsed)
  
     # git is so tricky!
     # if the path is like ssh://foo:22/some/path then it works, but
     # it needs the ssh://
     # If the path is like ssh://foo:some/path then it works, but
     # only if you remove the ssh://
    if parsed.protocol:
        parsed.protocol = protocolGit.sub('', parsed.protocol)
  
    # figure out what we should check out.
    checkout = parsed.hash and parsed.hash[1:] or 'master'
    parsed.hash = ''
  
    returnedUrl = None
    if altered:
        if protocolGitHttps.match(u) and pathnameNotNumbers.match(parsed.pathname):
            returnedUrl = protocolManipulator.replace('\1/\2', u)
        elif protocolGitFile.match(u):
            returnedUrl = protocolGitFile.replace('', u)
        else:
            returnedUrl = protocolGitSsh.replace('', u)
        returnedUrl = urlHash.replace('', returnedUrl)
    else:
      returnedUrl = urlunformat(parsed)
  
    return {
      url: returnedUrl,
      branch: checkout
    }
