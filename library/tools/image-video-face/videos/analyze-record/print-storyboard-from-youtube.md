---
id: print-storyboard-from-youtube
name: Print Storyboard from Youtube
description: 'OSINT tool: Print Storyboard from Youtube.'
url: javascript:(function(){a=ytplayer.config.args.storyboard_spec;if(!a){alert("Sorry we cannot process this YouTube video. Could you please try another one");exit();}b=a.split("|");base=b[0].split("$")[0]+"2/M";c=b[3].split("%23");sigh=c[c.length-1];var imgs="";t=ytplayer.config.args.length_seconds;n=Math.ceil(c[2]/(c[3]*c[4]));for(i=0;i<n;i++){imgs+="<PICTURE='"+base+i+".jpg%3Fsigh="+sigh+"'><br/>";}var title=ytplayer.config.args.title;msg="<body style='background-color:#444;color:#eee;margin:20px%20auto;width:90%;text-align:center'%3E%3Ch2%3ETITLE%3C/h2%3E%3Cdiv%3EIMAGES%3C/div%3E%3Cbr/%3E%3Cem%3E%3Ca%20href='http://labnol.org/?p=28217'%20style='text-decoration:none;color:#fff;font-style:bold'%3EPrinted%20using%20the%20YouTube%20bookmarklet.%3C/a%3E%3C/em%3E%3C/body%3E%22;msg=msg.replace(%22TITLE%22,title).replace(%22IMAGES%22,imgs).replace(/PICTURE/g,%22img%20src%22);var%20labnol=window.open();labnol.document.open();labnol.document.write(msg);labnol.document.close();})();
category: image-video-face
path:
- image-video-face
- videos
- analyze-record
bestFor: ''
input: ''
output: ''
selectorsIn: []
selectorsOut: []
status: unknown
pricing: free
opsec: unknown
opsecNote: ''
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: high
coverage: []
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases: []
tags: []
source: arf-seed
lastVerified: ''
enrichment: stub
---

# Print Storyboard from Youtube

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** javascript:(function(){a=ytplayer.config.args.storyboard_spec;if(!a){alert("Sorry we cannot process this YouTube video. Could you please try another one");exit();}b=a.split("|");base=b[0].split("$")[0]+"2/M";c=b[3].split("%23");sigh=c[c.length-1];var imgs="";t=ytplayer.config.args.length_seconds;n=Math.ceil(c[2]/(c[3]*c[4]));for(i=0;i<n;i++){imgs+="<PICTURE='"+base+i+".jpg%3Fsigh="+sigh+"'><br/>";}var title=ytplayer.config.args.title;msg="<body style='background-color:#444;color:#eee;margin:20px%20auto;width:90%;text-align:center'%3E%3Ch2%3ETITLE%3C/h2%3E%3Cdiv%3EIMAGES%3C/div%3E%3Cbr/%3E%3Cem%3E%3Ca%20href='http://labnol.org/?p=28217'%20style='text-decoration:none;color:#fff;font-style:bold'%3EPrinted%20using%20the%20YouTube%20bookmarklet.%3C/a%3E%3C/em%3E%3C/body%3E%22;msg=msg.replace(%22TITLE%22,title).replace(%22IMAGES%22,imgs).replace(/PICTURE/g,%22img%20src%22);var%20labnol=window.open();labnol.document.open();labnol.document.write(msg);labnol.document.close();})();
- **Best for:** —
- **Input → Output:** ? → ?
- **OpSec:** unknown. 

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
