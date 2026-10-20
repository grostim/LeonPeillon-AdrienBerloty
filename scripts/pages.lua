-- Conserve les repères photographiques dans le source LaTeX, sans les imprimer.
local function page_comment(el, inline)
  if el.format == 'html' and el.text:match('^<!%-%-') then
    local comment = '% ' .. el.text:gsub('^<!%-%-%s*', ''):gsub('%s*%-%->$', '') .. '\n'
    if inline then return pandoc.RawInline('latex', comment) end
    return pandoc.RawBlock('latex', comment)
  end
end
function RawBlock(el) return page_comment(el, false) end
function RawInline(el) return page_comment(el, true) end
