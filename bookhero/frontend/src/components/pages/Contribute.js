import React, { useState } from 'react'
import axios from 'axios'
import { faSearch } from '@fortawesome/pro-regular-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import Loading from '../common/Loading'

const BookSearchBar = props => {
  const [searchTerm, setSearchTerm] = useState('')

  const styles = {
    'button:hover': {
      backgroundColor: '#ced4da'
    }
  }

  const handleChange = event => {
    const text = event.target.value
    setSearchTerm(text)
  }

  return (
    <div>
      <form
        className='input-group mb-3'
        css={styles}
        onSubmit={props.handleSubmit(searchTerm)}
      >
        <input
          onChange={handleChange}
          type='text'
          className='form-control'
          value={searchTerm}
          placeholder='Search Book Titles'
          aria-label='Search Book Titles'
          aria-describedby='searchAddOn'
        />
        <div className='input-group-append'>
          <button
            className='btn btn-info'
            id='searchAddOn'
            type='submit'
            css={{ padding: '.75rem 1.25rem' }}
          >
            <FontAwesomeIcon icon={faSearch} size='lg' />
          </button>
        </div>
      </form>
    </div>
  )
}

const SearchResult = props => {
  const styles = {
    display: 'flex',
    '&:hover': {
      backgroundColor: '#eceeef'
    }
  }

  return (
    <div className='list-group-item' css={styles}>
      <img
        css={{
          marginRight: 15,
          maxWidth: 55,
          width: 'auto',
          alignSelf: 'center'
        }}
        src={`http://covers.openlibrary.org/b/id/${props.result.cover_i}-M.jpg`}
      />
      <div>
        <h5>{props.result.title}</h5>
        <p>
          {props.result.author_name !== undefined
            ? props.result.author_name.join(', ')
            : ''}
        </p>
      </div>
    </div>
  )
}

const SearchResults = props => {
  return (
    <div className='list-group'>
      {props.results.map((result, index) => (
        <SearchResult result={result} key={index} />
      ))}
    </div>
  )
}

const Contribute = props => {
  const [searchResults, setSearchResults] = useState([])
  const [isLoading, setIsLoading] = useState(false)

  const handleSubmit = searchTerm => async event => {
    event.preventDefault()
    try {
      if (searchTerm !== '') {
        setIsLoading(true)
        let result = await axios.get(
          `http://openlibrary.org/search.json?title=${encodeURIComponent(
            searchTerm
          )}`
        )
        console.log(result.data.docs)
        setSearchResults(result.data.docs.slice(0, 5))
        setIsLoading(false)
      }
    } catch (error) {
      console.log(error)
    }
  }

  const displayedSearchResults = isLoading ? (
    <Loading />
  ) : (
    <SearchResults results={searchResults} />
  )

  return (
    <div>
      <div css={{ marginTop: 25 }}>
        <h4>Search</h4>
        <BookSearchBar handleSubmit={handleSubmit} />
        {displayedSearchResults}
      </div>
    </div>
  )
}

export default Contribute
