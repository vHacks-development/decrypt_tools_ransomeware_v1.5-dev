import base64
exec(base64.b64decode(b'IyEvYmluL3B5dGhvbgojY29kaW5nOiB1dGYtOAoKaW1wb3J0IG9zLCBzeXMsIHRpbWUsIGJhc2U2NCwgc2h1dGlsLCBqc29uLCByZWFkbGluZSwgcmFuZG9tCgphcnJheSA9IFtdCgpjbGFzcyBhdXRvKG9iamVjdCk6CglkZWYgX19pbml0X18oc2VsZiwgb3B0aW9ucyk6CgkJc2VsZi5vcHRpb25zID0gc29ydGVkKG9wdGlvbnMpCgkKCWRlZiBjb21wbGV0ZShzZWxmLCB0ZXh0LCBzdGF0ZSk6CgkJaWYgc3RhdGUgPT0gMDoKCQkJaWYgdGV4dDoKCQkJCXNlbGYubWF0Y2hlcyA9IFtzIGZvciBzIGluIHNlbGYub3B0aW9ucyBpZiBzIGFuZCBzLnN0YXJ0c3dpdGgodGV4dCldCgkJCWVsc2U6CgkJCQlzZWxmLm1hdGNoZXMgPSBzZWxmLm9wdGlvbnNbOl0KCQl0cnk6CgkJCXJldHVybiBzZWxmLm1hdGNoZXNbc3RhdGVdCgkJZXhjZXB0IEluZGV4RXJyb3I6CgkJCXJldHVybiBOb25lCgpkZWYgY29tcGxldGUoYXJyYXkpOgoJY29tcGxldGVyID0gYXV0byhhcnJheSkKCXJlYWRsaW5lLnNldF9jb21wbGV0ZXIoY29tcGxldGVyLmNvbXBsZXRlKQoJcmVhZGxpbmUucGFyc2VfYW5kX2JpbmQoJ3RhYjpjb21wbGV0ZScpCgpkZWYgbG9hZGluZ1NjcmVlbihtc2csIG1zZ0lmRG9uZSA9ICIgICAgIik6CgliYXJzID0gWwoJCWYiWypdIHttc2d9IC4gICAtIiwKCQlmIlsqXSB7bXNnfSAuLiAgfCIsCgkJZiJbKl0ge21zZ30gLi4uIFxcIiwKCQlmIlsqXSB7bXNnfSAuICAgLyIsCgkJZiJbKl0ge21zZ30gLiAgIC0iLAoJCWYiWypdIHttc2d9IC4uICB8IiwKCQlmIlsqXSB7bXNnfSAuLi4gXFwiLAoJCWYiWypdIHttc2d9IC4gICAvIiwKCQlmIlsqXSB7bXNnfSAuICAgLSIsCgkJZiJbKl0ge21zZ30gLi4gIHwiLAoJCWYiWypdIHttc2d9IC4uLiBcXCIsCgkJZiJbKl0ge21zZ30gLiAgIC8iLAoJCWYiWypdIHttc2d9IC4gICAtIiwKCQlmIlsqXSB7bXNnfSAuLiAgfCIsCgkJZiJbKl0ge21zZ30gLi4uIFxcIiwKCQlmIlsqXSB7bXNnfSAuICAgLyIsCgkJZiJbKl0ge21zZ30gLiAgIC0iLAoJCWYiWypdIHttc2d9IC4uICB8IiwKCQlmIlsqXSB7bXNnfSAuLi4gXFwiLAoJCWYiWypdIHttc2d9IC4gICAvIiwKCQlmIlsqXSB7bXNnfSAuICAgLSIsCgkJZiJbKl0ge21zZ30gLi4gIHwiLAoJCWYiWypdIHttc2d9IC4uLiBcXCIsCgkJZiJbKl0ge21zZ30gLiAgIC8iLAoJCWYiWypdIHttc2d9IC4uLiB7bXNnSWZEb25lfSIKCV0KCWZvciBpIGluIHJhbmdlKGxlbihiYXJzKSk6CgkJdGltZS5zbGVlcCgxLi9yYW5kb20ucmFuZGludCgxLCAxMCkpCgkJc3lzLnN0ZG91dC53cml0ZShmIlxye2JhcnNbaV19IikKCQlzeXMuc3Rkb3V0LmZsdXNoKCkKCXByaW50KCIiKQoJdGltZS5zbGVlcCgyKQoKYmFubmVyID0gIiIiCiAgX19fICBfX18gIF8gXyAgX19fICBfX18gIF9fIF9fICBfX18gIF8gXyBfICBfX18gIF9fXyAgX19fIAogfCAuIFx8IC4gfHwgXCB8LyBfXz58IC4gfHwgIFwgIFx8IF9fPnwgfCB8IHx8IC4gfHwgLiBcfCBfXz4KIHwgICAvfCAgIHx8ICAgfFxfXyBcfCB8IHx8ICAgICB8fCBfPiB8IHwgfCB8fCAgIHx8ICAgL3wgXz4gCiB8X1xfXHxffF98fF9cX3w8X19fL2BfX18nfF98X3xffHxfX18+fF9fL18vIHxffF98fF9cX1x8X19fPiBEZWNyeXB0LVRvb2xzCiAgICBDb2RlIGJ5IEB2eGluLmRldiAgICAgIFsgcHl0aG9uIF0gICAgIHZlcnNpb24gMS41LWRldgoiIiIKCmRlZiBzdGFydEJhbm5lcigpOgoJcHJpbnQoYmFubmVyKQoKb3Muc3lzdGVtKCJjbGVhciIpCnRpbWUuc2xlZXAoMSkKc3RhcnRCYW5uZXIoKQpsb2FkaW5nU2NyZWVuKCJTdGFydCBkZWNyeXB0aW5nIikKCmlmIG9zLnBhdGguZXhpc3RzKCIucmFuc29tZXdhcmUvLmRlY3J5cHQua2V5Iik6Cgl1c2VyS2V5ID0gaW5wdXQoIls/XSBLZXk6ICIpCglmS2V5ID0ganNvbi5sb2FkcyhvcGVuKCIucmFuc29tZXdhcmUvLmRlY3J5cHQua2V5IiwgInIiKS5yZWFkKCkpWyJrZXkiXQoJaWYgdXNlcktleSA9PSBmS2V5OgoJCW51bSA9IDAKCQlsb2FkaW5nU2NyZWVuKGYiRGVjcnlwdCBhbGwgZmlsZXMiKQoJCWZvciBwYXRoIGluIGpzb24ubG9hZHMob3BlbigiLnJhbnNvbWV3YXJlLy5wYXRocy5qc29uIiwgInIiKS5yZWFkKCkpWyJwYXRocyJdOgoJCQlpZiBvcy5wYXRoLmV4aXN0cyhwYXRoKToKCQkJCWZvciBmaWxlIGluIG9zLmxpc3RkaXIoZiIucmFuc29tZXdhcmUvLnNhdmUve3BhdGh9Iik6CgkJCQkJaWYgZmlsZVstMTI6XSA9PSAiLmpwZy5lbmNyeXB0IiBvciBmaWxlWy0xMjpdID09ICIucG5nLmVuY3J5cHQiIG9yIGZpbGVbLTEyOl0gPT0gIi5tcDQuZW5jcnlwdCIgb3IgZmlsZVstMTI6XSA9PSAiLnBkZi5lbmNyeXB0IiBvciBmaWxlWy0xMjpdID09ICIubXAzLmVuY3J5cHQiIG9yIGZpbGVbLTEyOl0gPT0gIi50eHQuZW5jcnlwdCI6CgkJCQkJCXdpdGggb3BlbihmIi5yYW5zb21ld2FyZS8uc2F2ZS97cGF0aH0ve2ZpbGV9IiwgInIiKSBhcyBmOgoJCQkJCQkJZGVjID0gYmFzZTY0LmI2NGRlY29kZShmLnJlYWQoKSkKCQkJCQkJCW9wZW4oZiJ7cGF0aH0ve2ZpbGV9Ils6LThdLCAid2IiKS53cml0ZShkZWMpCgkJCQkJCQludW0gKz0gMQoJCQkJCWVsc2U6CgkJCQkJCXBhc3MKCQkJZWxzZToKCQkJCXBhc3MKCQlwcmludCgiXDAzM1tBWypdIERlY3J5cHQgYWxsIGZpbGVzIC4uLiBkb25lIikKCQlzaHV0aWwucm10cmVlKCIucmFuc29tZXdhcmUvLnNhdmUvc2RjYXJkIikKCQlvcy5yZW1vdmUoIi5yYW5zb21ld2FyZS8uZGVjcnlwdC5rZXkiKQoJCQoJCSNNZXNzYWdlIFdoZW4gRG9uZSBEZWNyeXB0CgkJcHJpbnQoZiJbKl0ge251bX0gRmlsZXMgaGF2ZSBiZWVuIGRlY3J5cHRlZFxuIikKCWVsc2U6CgkJcHJpbnQoIlsqXSBUaGUga2V5IHlvdSBlbnRlcmVkIGlzIGluY29ycmVjdCIpCmVsc2U6CglwcmludCgiWypdIFlvdSBjYW4ndCBkZWNyeXB0IGl0Iik='))