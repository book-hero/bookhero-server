import React from 'react'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faChevronLeft } from '@fortawesome/pro-regular-svg-icons'

const BookInfo = ({ book }) => {
  console.log(book)
  book = {
    author: ['J. K. Rowling'],
    coverId: 8267078,
    isbns: ['9513111466', '9992747633'],
    publishYears: [1997],
    publishers: ['Yediʻot Aḥaronot'],
    title: "Harry Potter and the Philosopher's Stone"
  }
  return (
    <div css={{ paddingTop: 15, display: 'flex' }}>
      <img src={`http://covers.openlibrary.org/b/id/${book.coverId}-M.jpg`} />
      <div css={{ paddingLeft: 15, paddingRight: 15 }}>
        <h4 className='card-title'>
          {book.title}
          <br />
          <small>{book.author}</small>
        </h4>
      </div>
    </div>
  )
}

export default BookInfo
