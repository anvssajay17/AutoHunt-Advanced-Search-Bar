import React from 'react';
import './Background.css';
import SearchBar from './SearchBar';

const Background = () => {
  return (
    <div className="wrapper">
      <div className="search-center">
        <SearchBar />
      </div>
      <div className="box">
        {Array.from({ length: 10 }).map((_, i) => (
          <div key={i}></div>
        ))}
      </div>
    </div>
  );
};

export default Background;
