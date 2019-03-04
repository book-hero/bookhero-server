// function debounce (func, wait, immediate) {
//   let timeout
//   return function () {
//     const args = arguments
//     const later = () => {
//       timeout = null
//       if (!immediate) func.apply(this, args)
//     }
//     const callNow = immediate && !timeout
//     clearTimeout(timeout)
//     timeout = setTimeout(later, wait)
//     if (callNow) func.apply(this, args)
//   }
// }

function debounce (func, wait, immediate) {
  var timeout
  return (function () {
    var context = this

    var args = arguments
    var later = function () {
      timeout = null
      if (!immediate) func.apply(context, args)
    }
    var callNow = immediate && !timeout
    clearTimeout(timeout)
    timeout = setTimeout(later, wait)
    if (callNow) func.apply(context, args)
  })()
}

export { debounce }
