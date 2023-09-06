from discord.ext import commands
from discord import FFmpegPCMAudio
from integrations.youtube import YouTubeIntegration
from cogs.music.queue import SongQueue
from cogs.playlist.manager import PlaylistManager


class MusicPlayer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.song_queue = SongQueue()
        self.youtube_integration = YouTubeIntegration(api_key="YOUR_YOUTUBE_API_KEY")
        self.current_voice_channel = None
        self.playlist_manager = None

    @commands.command(name='join')
    async def join(self, ctx):
        """Bot joins the voice channel."""
        if ctx.author.voice:
            self.current_voice_channel = await ctx.author.voice.channel.connect()
            self.playlist_manager = PlaylistManager(ctx.author.id)

    @commands.command(name='leave')
    async def leave(self, ctx):
        """Bot leaves the voice channel."""
        await self.current_voice_channel.disconnect()
        self.current_voice_channel = None
        self.playlist_manager = None

    @commands.command(name='play')
    async def play(self, ctx, *, song_name: str):
        """Play a song from YouTube."""
        song_url = self.youtube_integration.search_song(song_name)
        if song_url:
            self.song_queue.add(song_url)
            # Stream the song using FFmpeg and discord.py's Audio Source
            audio_source = FFmpegPCMAudio(executable="ffmpeg", source=song_url)
            self.current_voice_channel.play(audio_source)
            await ctx.send(f"Playing {song_name}!")
        else:
            await ctx.send(f"Couldn't find {song_name} on YouTube.")

    @commands.command(name='pause')
    async def pause(self, ctx):
        """Pause the currently playing song."""
        self.current_voice_channel.pause()
        await ctx.send("Paused the current song.")

    @commands.command(name='resume')
    async def resume(self, ctx):
        """Resume the paused song."""
        self.current_voice_channel.resume()
        await ctx.send("Resumed the current song.")

    @commands.command(name='add_to_playlist')
    async def add_to_playlist(self, ctx, *, song_name: str):
        """Add a song to the user's playlist."""
        song_url = self.youtube_integration.search_song(song_name)
        if song_url:
            playlist_manager = PlaylistManager(ctx.author.id)
            playlist_manager.add_song_to_playlist(song_name, song_url)
            await ctx.send(f"Added {song_name} to your playlist!")
        else:
            await ctx.send(f"Couldn't find {song_name} on YouTube.")

    @commands.command(name='show_playlist')
    async def show_playlist(self, ctx):
        """Show the user's playlist."""
        playlist = self.playlist_manager.get_user_playlist()
        formatted_playlist = "\n".join([f"{i + 1}. {song}" for i, song in enumerate(playlist)])
        await ctx.send(f"Your Playlist:\n{formatted_playlist}")

    @commands.command(name='skip')
    async def skip(self, ctx):
        """Skip the currently playing song."""
        self.song_queue.skip()
        next_song = self.song_queue.get_next_song()
        if next_song:
            audio_source = FFmpegPCMAudio(executable="ffmpeg", source=next_song)
            self.current_voice_channel.play(audio_source)
            await ctx.send("Skipped to the next song.")
        else:
            await self.stop(ctx)  # Stops playback if no more songs in the queue

    @commands.command(name='stop')
    async def stop(self, ctx):
        """Stop playing and clear the song queue."""
        self.song_queue.clear()
        self.current_voice_channel.stop()
        await ctx.send("Stopped playing and cleared the queue.")

    @commands.command(name='shuffle')
    async def shuffle(self, ctx):
        """Shuffle the song queue."""
        self.song_queue.shuffle()
        await ctx.send("Shuffled the song queue.")
