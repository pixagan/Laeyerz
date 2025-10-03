import React from 'react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';


const MarkdownViewer = ({markdown_in}) => {
  return (
    <div style={{ padding: '2rem', fontFamily: 'sans-serif', maxWidth: '800px', margin: 'auto', textAlign: 'left' }}>
      <ReactMarkdown remarkPlugins={[remarkGfm]}>{markdown_in}</ReactMarkdown>
    </div>
  );
};

export default MarkdownViewer;
