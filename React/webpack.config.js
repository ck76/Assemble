var config = {
    // ���������ļ�
    entry: './main.js',

    // ���ô�������path��������ļ��У�filename����������ļ�������
    output: {
        path: './',
        filename: 'index.js'
    },

    // ���÷������˿ں�
    devServer: {
        inline: true,
        port: 7777
    },

    // ����ģ��Ĵ����߼�����loaders���������
    module: {
        loaders: [
            {
                test: /\.jsx?$/,
                exclude: /node_modules/,
                loader: 'babel',
                query: {
                    presets: ['es2015', 'react']
                }
            }
        ]
    }
}

module.exports = config;
