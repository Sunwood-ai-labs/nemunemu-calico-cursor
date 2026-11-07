import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'Nemunemu Calico Cursor',
  description: 'A sleepy calico cat & mint pointer animated cursor theme for Windows 10 / 11',
  base: '/nemunemu-calico-cursor/',
  cleanUrls: true,
  head: [
    ['link', { rel: 'icon', type: 'image/svg+xml', href: '/nemunemu-calico-cursor/icon.svg' }]
  ],
  themeConfig: {
    logo: '/icon.svg',
    socialLinks: [
      { icon: 'github', link: 'https://github.com/Sunwood-ai-labs/nemunemu-calico-cursor' }
    ]
  },
  locales: {
    root: {
      label: 'English',
      lang: 'en-US',
      title: 'Nemunemu Calico Cursor',
      description: 'A sleepy calico cat & mint pointer animated cursor theme for Windows 10 / 11',
      themeConfig: {
        nav: [
          { text: 'Home', link: '/' },
          { text: 'Getting Started', link: '/guide/getting-started' },
          { text: 'Cursors & Hotspots', link: '/guide/cursors-and-hotspots' },
          { text: 'Customization', link: '/guide/customization' }
        ],
        sidebar: [
          {
            text: 'Guide',
            items: [
              { text: 'Getting Started', link: '/guide/getting-started' },
              { text: 'Cursors & Hotspots', link: '/guide/cursors-and-hotspots' },
              { text: 'Build & Customization', link: '/guide/customization' }
            ]
          }
        ],
        footer: {
          message: 'Released under the MIT License.',
          copyright: 'Copyright © 2026 Sunwood-ai-labs'
        }
      }
    },
    ja: {
      label: '日本語',
      lang: 'ja-JP',
      link: '/ja/',
      title: 'ねむねむ三毛ネコ カーソル',
      description: 'ミントカラーのポインタに寄り添う「ねむねむ三毛ネコ」の Windows 10 / 11 用アニメーションマウスカーソルテーマ',
      themeConfig: {
        nav: [
          { text: 'ホーム', link: '/ja/' },
          { text: '導入ガイド', link: '/ja/guide/getting-started' },
          { text: 'カーソル＆ホットスポット', link: '/ja/guide/cursors-and-hotspots' },
          { text: 'ビルド＆カスタマイズ', link: '/ja/guide/customization' }
        ],
        sidebar: [
          {
            text: 'ガイド',
            items: [
              { text: '導入ガイド (Getting Started)', link: '/ja/guide/getting-started' },
              { text: 'カーソル一覧とホットスポット', link: '/ja/guide/cursors-and-hotspots' },
              { text: 'ビルドとカスタマイズ', link: '/ja/guide/customization' }
            ]
          }
        ],
        footer: {
          message: 'MIT License の下で公開されています。',
          copyright: 'Copyright © 2026 Sunwood-ai-labs'
        }
      }
    }
  }
})
