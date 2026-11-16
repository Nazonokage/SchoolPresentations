// Presentation-only highlighting: escaping never changes copied source text.
const escape=s=>s.replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;');
export function highlight(source){
 const re=/<!--[\s\S]*?-->|\/\*[\s\S]*?\*\/|\/\/[^\n\r]*|"(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*'|`(?:\\.|[^`\\])*`|<\/?[A-Za-z][\w:-]*|\b(?:const|let|var|function|return|if|else|for|while|of|in|await|async|new|throw|try|catch|finally|class|extends|import|from|export|default|interface|type|true|false|null|undefined|switch|case|break|continue)\b|\b\d+(?:\.\d+)?\b|\b[A-Za-z_$][\w$]*(?=\s*\()/g;
 let out='',last=0;
 for(const m of source.matchAll(re)){
  out+=escape(source.slice(last,m.index));const t=m[0];
  const kind=/^(?:\/\/|\/\*|<!--)/.test(t)?'comment':/^["'`]/.test(t)?'string':/^</.test(t)?'tag':/^\d/.test(t)?'number':/^(?:const|let|var|function|return|if|else|for|while|of|in|await|async|new|throw|try|catch|finally|class|extends|import|from|export|default|interface|type|true|false|null|undefined|switch|case|break|continue)$/.test(t)?'keyword':'function';
  out+='<span class="syntax-'+kind+'">'+escape(t)+'</span>';last=m.index+t.length;
 }
 return out+escape(source.slice(last));
}
