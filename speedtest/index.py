import speedtest

st = speedtest.Speedtest()

download = st.download()
upload = st.upload()

print(f"Download Speed: {download}")
print(f"Upload Speed: {upload}")

