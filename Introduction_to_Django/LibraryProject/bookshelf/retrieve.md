
---

## 📄 **retrieve.md**

```markdown
# Retrieve Book

```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title
book.author
book.publication_year
# Expected output:
# book.title => '1984'
# book.author => 'George Orwell'
# book.publication_year => 1949
