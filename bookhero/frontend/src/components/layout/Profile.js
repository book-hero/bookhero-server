import React from 'react'
import ProfilePicture from '../common/ProfilePicture'

const profileStyles = {
  display: 'flex',
  flexDirection: 'column',
  alignItems: 'center'
}

const Profile = props => (
  <div id='profile' css={profileStyles}>
    <ProfilePicture />
    <h4>User Name</h4>
  </div>
)

export default Profile
