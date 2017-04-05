# python-normalize-git-url

You have a bunch of Git URLs. You want to convert them to a canonical representation, maybe so that you doesn't end up creating a bunch of superfluous cached origins. You use this package.

python-normalize-git-url is a direct port of the [normalize-git-url][] npm package. Any behavior that is not the same is considered a bug.

## Usage

```python
import ngu

normalized = ngu("git+ssh://git@github.com:organization/repo.git#hashbrowns")
# get back:
# {
#   url : "ssh://git@github.com/organization/repo.git",
#   branch : "hashbrowns" # did u know hashbrowns are delicious?
# }
```

## API

There's just the one function, and all it takes is a single parameter, a non-normalized Git URL.

### ngu.normalizeGitUrl(url)

* `url` {String} The Git URL (very loosely speaking) to be normalized.

Returns an object with the following format:

* `url` {String} The normalized URL.
* `branch` {String} The treeish to be checked out once the repo at `url` is
  cloned. It doesn't have to be a branch, but it's a lot easier to intuit what
  the output is for with that name.

## Limitations

Right now this doesn't try to special-case GitHub too much -- it doesn't ensure that `.git` is added to the end of URLs, it doesn't prefer `https:` over `http:` or `ssh:`, it doesn't deal with redirects, and it doesn't try to resolve symbolic names to treeish hashcodes. For now, it just tries to account for minor differences in representation.

## License

This module borrows _very_ liberally (and shamelessly) from the original [normalize-git-url][]. I owe its authors a debt of gratitude, so this project is ISC licensed, just like the original.

 [normalize-git-url]: https://github.com/npm/normalize-git-url
