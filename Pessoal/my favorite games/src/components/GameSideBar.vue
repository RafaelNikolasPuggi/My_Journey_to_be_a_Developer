<template>
    <nav class="bg-white shadow-lg h-screen fixed top-0 left-0 min-w-[220px] py-6 px-6 font-[sans-serif] flex flex-col overflow-auto">
      
      <div class="relative bg-gray-100 px-4 py-3 rounded-md mt-14">
        <svg xmlns="http://www.w3.org/2000/svg" fill="#3949ab" class="w-4 mr-4 inline" viewBox="0 0 118.783 118.783">
          <path
            d="M115.97 101.597 88.661 74.286a47.75 47.75 0 0 0 7.333-25.488c0-26.509-21.49-47.996-47.998-47.996S0 22.289 0 48.798c0 26.51 21.487 47.995 47.996 47.995a47.776 47.776 0 0 0 27.414-8.605l26.984 26.986a9.574 9.574 0 0 0 6.788 2.806 9.58 9.58 0 0 0 6.791-2.806 9.602 9.602 0 0 0-.003-13.577zM47.996 81.243c-17.917 0-32.443-14.525-32.443-32.443s14.526-32.444 32.443-32.444c17.918 0 32.443 14.526 32.443 32.444S65.914 81.243 47.996 81.243z"
            data-original="#000000" />
        </svg>
        <input class="text-sm text-[#3949ab] outline-none bg-transparent px-1 max-w-[130px]" placeholder="Search..." />
      </div>
      <ul class="space-y-8 pl-3 flex-1 mt-10">
        <li>
          <a href="javascript:void(0)" class="text-[#3949ab] font-semibold text-sm flex items-center rounded-md left-0 hover:left-1 relative transition-all">
            <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" class="w-[18px] h-[18px] mr-4" viewBox="0 0 512 512">
              <path
                d="M197.332 170.668h-160C16.746 170.668 0 153.922 0 133.332v-96C0 16.746 16.746 0 37.332 0h160c20.59 0 37.336 16.746 37.336 37.332v96c0 20.59-16.746 37.336-37.336 37.336zM37.332 32A5.336 5.336 0 0 0 32 37.332v96a5.337 5.337 0 0 0 5.332 5.336h160a5.338 5.338 0 0 0 5.336-5.336v-96A5.337 5.337 0 0 0 197.332 32zm160 480h-160C16.746 512 0 495.254 0 474.668v-224c0-20.59 16.746-37.336 37.332-37.336h160c20.59 0 37.336 16.746 37.336 37.336v224c0 20.586-16.746 37.332-37.336 37.332zm-160-266.668A5.337 5.337 0 0 0 32 250.668v224A5.336 5.336 0 0 0 37.332 480h160a5.337 5.337 0 0 0 5.336-5.332v-224a5.338 5.338 0 0 0-5.336-5.336zM474.668 512h-160c-20.59 0-37.336-16.746-37.336-37.332v-96c0-20.59 16.746-37.336 37.336-37.336h160c20.586 0 37.332 16.746 37.332 37.336v96C512 495.254 495.254 512 474.668 512zm-160-138.668a5.338 5.338 0 0 0-5.336 5.336v96a5.337 5.337 0 0 0 5.336 5.332h160a5.336 5.336 0 0 0 5.332-5.332v-96a5.337 5.337 0 0 0-5.332-5.336zm160-74.664h-160c-20.59 0-37.336-16.746-37.336-37.336v-224C277.332 16.746 294.078 0 314.668 0h160C495.254 0 512 16.746 512 37.332v224c0 20.59-16.746 37.336-37.332 37.336zM314.668 32a5.337 5.337 0 0 0-5.336 5.332v224a5.338 5.338 0 0 0 5.336 5.336h160a5.337 5.337 0 0 0 5.332-5.336v-224A5.336 5.336 0 0 0 474.668 32zm0 0"
                data-original="#000000" />
            </svg>
            <span>Dashboard</span>
          </a>
        </li>
        <li>
          <a href="javascript:void(0)" class="text-[#3949ab] font-semibold text-sm flex items-center rounded-md left-0 hover:left-1 relative transition-all">
            <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" class="w-[18px] h-[18px] mr-4" viewBox="0 0 16 16">
              <path
                d="M13 .5H3A2.503 2.503 0 0 0 .5 3v10A2.503 2.503 0 0 0 3 15.5h10a2.503 2.503 0 0 0 2.5-2.5V3A2.503 2.503 0 0 0 13 .5ZM14.5 13a1.502 1.502 0 0 1-1.5 1.5H3A1.502 1.502 0 0 1 1.5 13v-.793l3.5-3.5 1.647 1.647a.5.5 0 0 0 .706 0L10.5 7.207V8a.5.5 0 0 0 1 0V6a.502.502 0 0 0-.5-.5H9a.5.5 0 0 0 0 1h.793L7 9.293 5.354 7.647a.5.5 0 0 0-.707 0L1.5 10.793V3A1.502 1.502 0 0 1 3 1.5h10A1.502 1.502 0 0 1 14.5 3Z"
                data-original="#000000" />
            </svg>
            <span>Insight</span>
          </a>
        </li>
        <li>
          <a href="javascript:void(0)" class="text-[#3949ab] font-semibold text-sm flex items-center rounded-md left-0 hover:left-1 relative transition-all">
            <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" class="w-[18px] h-[18px] mr-4" viewBox="0 0 20 20">
              <path
                d="M4.9 8h10.2c1.2 0 1.4-.2 1.7-1.4C17 4.7 16.4 4 15.2 4H4.8C3.6 4 3 4.7 3 6.6 3.4 7.8 3.7 8 4.9 8ZM18 9c-.1 0-.1 0 0 0H2c-.1 0-.1 0 0 0-1.1 0-1.8 1-.9 2l.9 1v3c0 1.7 1.3 3 3 3h10c1.7 0 3-1.3 3-3v-3l.9-1c1-1 .2-2-.9-2ZM7.2 13.6a.6.6 0 0 1-.6.4h-.4a.6.6 0 0 1-.6-.4L4.5 11.7a.5.5 0 1 1 1-.3l.6 2 1.6-4.4a.5.5 0 0 1 1 0l.8 2.6h.7a.5.5 0 1 1 0 1h-1a.6.6 0 0 1-.6-.4l-.4-1.2ZM14 14h-1a1 1 0 0 1 0-2h1a1 1 0 0 1 0 2Zm-1-3a.5.5 0 1 1 0-1h2a.5.5 0 1 1 0 1h-2Z"
                data-original="#000000" />
            </svg>
            <span>Reports</span>
          </a>
        </li>
        <li>
          <a href="javascript:void(0)" class="text-[#3949ab] font-semibold text-sm flex items-center rounded-md left-0 hover:left-1 relative transition-all">
            <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" class="w-[18px] h-[18px] mr-4" viewBox="0 0 20 20">
              <path
                d="M10 0a4.996 4.996 0 0 0-4 8.326V14a1 1 0 0 1-.553.894l-2 1a1 1 0 0 0 .447 1.894h12.212a1 1 0 0 0 .447-1.894l-2-1A1 1 0 0 1 14 14V8.326A4.996 4.996 0 0 0 10 0Zm2.466 16H7.534A2.98 2.98 0 0 0 6 14.618V9.878a4.976 4.976 0 0 0 2.634.733 4.976 4.976 0 0 0 2.634-.733v4.74c0 .438-.177.86-.502 1.181ZM10 8a3 3 0 1 1 0-6 3 3 0 0 1 0 6Z"
                data-original="#000000" />
            </svg>
            <span>Notifications</span>
          </a>
        </li>
        <li>
          <a href="javascript:void(0)" class="text-[#3949ab] font-semibold text-sm flex items-center rounded-md left-0 hover:left-1 relative transition-all">
            <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" class="w-[18px] h-[18px] mr-4" viewBox="0 0 48 48">
              <path
                d="M44 4H16a4 4 0 0 0-4 4v28.628l-4.314-4.313a4 4 0 0 0-5.656 5.656l11.313 11.314A3.97 3.97 0 0 0 16 47.998h.002a3.97 3.97 0 0 0 2.828-1.17L30.142 35.516a4 4 0 1 0-5.656-5.656l-4.314 4.313V8H44v22.272a4 4 0 1 0 8 0V8a12.013 12.013 0 0 0-12-12z"
                data-original="#000000" />
            </svg>
            <span>Messages</span>
          </a>
        </li>
      </ul>
    </nav>
  </template>
  
  <script>
  export default {
    name: "GameSideBar",
  };
  </script>
  
  <style scoped>
  nav {
    display: flex;
    flex-direction: column;
  }
  </style>
  