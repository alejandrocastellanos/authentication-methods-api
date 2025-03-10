import uvicorn

if __name__ == '__main__':
    uvicorn.run('src:app',
                host='0.0.0.0',
                port=7373,
                reload=True,
                access_log=True,
                log_level='debug'
                )
